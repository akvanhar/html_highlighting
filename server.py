import os

from flask import (Flask, render_template, request)

from flask_debugtoolbar import DebugToolbarExtension

from jinja2 import StrictUndefined

from cgi import escape

from parse import get_html

app = Flask(__name__)
app.secret_key = os.environ['FLASK_TOKEN']

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/url_handler')
def url_handler():
	url = request.args.get('url')
	source_html = str(get_html(url))
	escaped_html = escape(source_html)
	return escaped_html

####################################################

PORT = int(os.environ.get("PORT", 5000))
DEBUG = "NO_DEBUG" not in os.environ

if __name__ == "__main__":
    # Set debug to true to have the toolbar extension run.
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ
    
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
