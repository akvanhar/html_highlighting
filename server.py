import os
from flask import (Flask, render_template, redirect, request, flash)
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from parse import get_html, encode_html, create_count, add_spans
import requests
import re


app = Flask(__name__)
app.secret_key = os.environ['FLASK_TOKEN']

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/url_handler')
def url_handler():
	# given user input URL, check if URL is valid,
	# parse HTML, store elements and frequencies in dictionary
	# encode HTML, add spans and return to template
	url = request.args.get('url')
	try:
		html_object = requests.get(url)
	except requests.exceptions.RequestException:
		return 'The URL you entered is invalid, or is having trouble connecting at this time.\
			    Please enter a new URL.'

	# decode requests unicode object
	html = get_html(html_object)

	# create dictionary of tags and counts
	tags = create_count(html)

	# excape < > and & characters so html can be displayed
	html = encode_html(html)

	# wrap individual tags with spans so they can be highlighted
	html = add_spans(html)
	
	return render_template('results.html', 
							url=url,
							html=html,
							tags=tags)

####################################################

PORT = int(os.environ.get("PORT", 5000))
DEBUG = "NO_DEBUG" not in os.environ

if __name__ == "__main__":
    # Set debug to true to have the toolbar extension run.
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ
    
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
