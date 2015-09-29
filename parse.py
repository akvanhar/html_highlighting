import requests
import urllib2
import cgi
import lxml.html

def get_html(html_object):
	# takes a url as a string and 
	# returns the html from that page as a string
	
	return html_object.text

def encode_html(html_string):
	# takes a string of html
	# returns an encoded string to display
	
	return cgi.escape(html_string)

def create_count(html_string):
	# takes a string of html
	# creates a tree using lxml.tree
	# returns a dictionary where key: tag and 
	# value: count of tag occurance

	tags = {}
	html_tree = lxml.html.fromstring(html_string)
	for element in html_tree.iter():
		if not tags.get(element.tag):
			tags[element.tag] = 0
		tags[element.tag] += 1
		element.tag = "span class="+element.tag+">&lt;"+element.tag+"&gt;</span><br"
		# element = "<span class="+element+">"+element+"</span>"
		print element.tag, type(element.tag)
	return tags


# span class=div>&lt;div&gt;</span><br