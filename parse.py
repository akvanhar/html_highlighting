import requests
import urllib2
import cgi

def get_html(html_object):
	# takes a url as a string and 
	# returns the html from that page as a string
	return html_object.text

def encode_html(html_string):
	# takes a string of html
	# returns an encoded string to display
	return cgi.escape(html_string)