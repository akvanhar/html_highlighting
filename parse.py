from bs4 import BeautifulSoup
import urllib2
import cgi

def get_html(url):
	# takes a url as a string and 
	# returns the html from that page as a string

	url = url
	page = urllib2.urlopen(url)
	html_string = str(BeautifulSoup(page.read()))
	return html_string

def encode_html(html_string):
	# takes a string of html
	# returns an encoded string to display
	return cgi.escape(html_string)