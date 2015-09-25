from flask import (Flask, render_template, request)

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
	return render_template('home.html')

####################################################

PORT = int(os.environ.get("PORT", 5000))
DEBUG = "NO_DEBUG" not in os.environ

if __name__ == "__main__":
    # Set debug to true to have the toolbar extension run.
    app.debug = DEBUG

    app.run(host='0.0.0.0', port=PORT)
