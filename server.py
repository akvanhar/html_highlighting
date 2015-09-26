import os

from flask import (Flask, render_template, request)

from flask_debugtoolbar import DebugToolbarExtension

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = os.environ['FLASK_TOKEN']

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
	return render_template('home.html')

@app.route('url_handler')
def url_handler():
	url = response.args.get('url')
	print url
	return url

####################################################

PORT = int(os.environ.get("PORT", 5000))
DEBUG = "NO_DEBUG" not in os.environ

if __name__ == "__main__":
    # Set debug to true to have the toolbar extension run.
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ
    
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
