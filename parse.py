import requests
import urllib2
import cgi
import lxml.html
import re

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
	out_html = ""
	html_tree = lxml.html.fromstring(html_string)
	for element in html_tree.iter():
		if not tags.get(element.tag):
			tags[element.tag] = 0
		tags[element.tag] += 1
	return tags

def add_spans(html):
	# wrap individual tags in span tags with specific classes.
	# eg. <span class="all-div"><div></span>
	def add_open_span(matchobj):
		return "<span class='all-%s'>%s" % (matchobj.group(1), matchobj.group())

	def add_close_span(matchobj):
		return "<span class='all-%s'>%s" % (matchobj.group(2), matchobj.group())

    # This is the regex pattern to find the element type: &lt;([A-Z|a-z]+[0-9]*)
    # replaces opening tags
	html = re.sub('&lt;([A-Z|a-z]+[0-9]*)', add_open_span, html)

	# replace closing tags, but don't include the / in theh class
	html = re.sub('&lt;(\/+)([A-Z|a-z]+[0-9]*)', add_close_span, html)
	html = html.replace("&gt;", "&gt;</span>")

	return html
# span class=div>&lt;div&gt;</span><br