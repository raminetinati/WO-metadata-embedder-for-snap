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
					if(str(td.text) != "None"):
						entry.append(td.text)
						#print "column: ",td.text
				except:
					pass;
			data.append(entry)

	for entry in data:
		print entry
						#pass;
	# extractedTables = tree.xpath('//*[@id="datatab2"]')
	# xpath1 = "//*/tr"

	# rows = tree.xpath(xpath1)
	# data = list()
	# for row in rows:
	#     data.append([c.text for c in row.getchildren()])
	    #print row.getchildren()[0].text_content()
	    #print row.getchildren()[0].get('text')
	#for item in data:
		#print item

	# for table in extractedTables:
	# 	#//*[@id="datatab2"]/tbody/tr[2]/td[1]/a
	# 	print table
	#print extractedTables;



def run():
	#get the tweets
	#filename = "test_tweets - Copy.csv"
	print "Getting HTML file"
	urlToRetrieve = "http://snap.stanford.edu/data/index.html"
	htmlTree = getHTMLPage(urlToRetrieve)
	parseHTMLForTables(htmlTree)






if __name__ == '__main__':
	#run the script
	run()