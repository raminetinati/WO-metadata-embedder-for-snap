# Author: Ramine Tinati - raminetinati@gmail.com
# Purpose: To embed Web Observatory metadata into SNAP
import glob
import os
import time
import sys
import json
from lxml import html
import requests
from datetime import datetime
from pyquery import PyQuery as pq
from lxml import etree
import urllib


def getHTMLPage(htmlURL):
	tree = pq(url=htmlURL)
	#print tree
	return tree


#Just for SNAP tables '//*[@id="datatab2"]') 
def parseHTMLForTables(tree):


	data = []
	tables = tree('#datatab2')
	print len(tables)
	for table in tables:
		for item in table:
			entry = []
			for td in item:
				for tr in td:
					try:
						if(str(tr.attrib['href']) != '#netTypes'):
							entry.append(str(tr.attrib['href']))
							entry.append(str(tr.text))
					 		#print "URL:", tr.attrib['href']
					 		#print "URL Text:", tr.text
					except:
						pass;
				try:
					#remove unwanted rows...
					if((str(td.text) != "None") and (str(td.text) != "Name") and (str(td.text) != "Number of items") and (str(td.text) != "Description") and (str(td.text) != "Nodes")  and (str(td.text) != "Edges")):
						entry.append(td.text)
						#print "column: ",td.text
				except:
					pass;

			if len(entry) > 3:
				data.append(entry)

	# for entry in data:
	# 	print entry

	return data

def createWOMetadata(datasets):

	htmlEntries = []
	for entry in datasets:
		entryHTML = "<div itemscope itemtype=\"http://schema.org/Dataset/WebObservatory\">"
		#link = entry[0];
		if(".html" not in entry[1]):
			title = entry[1]
		else:
			title = entry[2]

		for atom in entry:
			if '.html' in atom:
				link = atom
		
		desc = ""
		for x in range(2, len(entry)):
			desc = desc + " " + entry[x]

		if("http" not in link):
			link = "http://snap.stanford.edu/data/"+link

		# print "title: " , title
		# print "link: " , link
		# print "desc: " , desc

		publisher = "<meta itemprop=\"http://schema.org/provider\" content=\"SNAP - Stanford\">"

		entryHTML = entryHTML + " <meta itemprop=\"http://schema.org/name\" content=\""+title+"\">"
		entryHTML = entryHTML + "  <meta itemprop=\"http://schema.org/url\" content=\""+link+"\">"
		entryHTML = entryHTML + "  <meta itemprop=\"http://schema.org/description\" content=\""+desc+"\">"
		entryHTML = entryHTML + publisher
		entryHTML = entryHTML +  "</div>"

		htmlEntries.append(entryHTML)

	output = open("metadata.html","w")
	for ht in htmlEntries:
		output.write(ht+"\n")
	output.close()

def run():
	#get the tweets
	#filename = "test_tweets - Copy.csv"
	print "Getting HTML file"
	urlToRetrieve = "http://snap.stanford.edu/data/index.html"
	htmlTree = getHTMLPage(urlToRetrieve)
	datasets = parseHTMLForTables(htmlTree)
	htmlToInsert = createWOMetadata(datasets)





if __name__ == '__main__':
	#run the script
	run()