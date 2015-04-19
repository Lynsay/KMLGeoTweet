#!/usr/bin/env python

'''
	File: geo_to_kml.py
	Version: 1.0
	Date: December 2014
	Author: Lynsay A. Shepherd
	License: MIT License (MIT)
	
	Description: This script converts the CSV to KML- open with Google Earth.
	#Downloaded my entire Twitter archive.
	#Ran a modified script from https://github.com/mshea/Parse-Twitter-Archive to parse the archive.  This was written by  Michael E. Shea at http://mikeshea.net/ This extracted all geolocation tweets- dumped these into CSV format.
	#My modified script is available from- https://github.com/Lynsay/Parse-Twitter-ArchiveCSV
'''

import csv
import xml.etree.cElementTree as ET
import datetime
import sys
import time

#for general information- tweet link structure:
#https://twitter.com/username/status/tweet_id_here

#set username variable- all tweets are mine
tweetUsername="USERNAME"


def generate_file_name():
#generate timestamp for KML file
	try:
		global newFileName
		print "***generating a file name***"
		ts = time.time()
		myTimestamp = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y_%H-%M-%S')
		#save in a folder called kml_files
		newFileName = "kml_files/"+tweetUsername+'_'+myTimestamp+'.kml'
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"
	
	

def generate_kml_file():
#start generating the KML file
	try:
		print "***generating a new KML file***"
		global kmlDeclaration, doc
		kmlDeclaration= ET.Element("kml")
		kmlDeclaration.set("xmlns", "http://www.opengis.net/kml/2.2")
		doc = ET.SubElement(kmlDeclaration, "Document")
		nameField = ET.SubElement(doc, "name")
		nameField.text = tweetUsername+".kml"

		#change the style for pins on the map
		style = ET.SubElement(doc, "Style")
		style.set("id", "additional_pin")
		iconstyle = ET.SubElement(style, "IconStyle")
		iconstyle.set("id", "mystyle")
		icon = ET.SubElement(iconstyle, "Icon")
		href = ET.SubElement(icon, "href")
		href.text = "http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png"
		scale = ET.SubElement(icon, "scale")
		scale.text = "1.0"
		
		#get the data
		open_csv_file()
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"	
	


def open_csv_file():
	try:
		#start reading in the relevant stuff from the geo CSV file
		print "***opening the CSV file***"
		with open('FILENAME.csv', 'rb') as f:
			mycsv = csv.reader(f)
	
			#ignore the first line of the generated geo csv file.
			#it contains the text id, date etc and greats a point labelled (0,0)
			mycsv.next()
		
			#start looping through the file
			for row in mycsv:
				single_tweet_data_array=create_single_tweet_array(row)
				add_placemarks_to_kml(single_tweet_data_array)
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"
		



def create_single_tweet_array(row):
	try:
		print "***reading new tweet***"
		#stick some data on the command line
		print "-------------"
		print "TweetID: "+row [0]+", time: "+ row [1]+", coord1: "+ row [3]+", coord2: "+row[4]
		print "Tweet: "+row[2]
		print "-------------\n"

		#assign each row to a variable
		tweetURL="https://twitter.com/"+tweetUsername+"/status/"+row [0]
		tweetTime=row [1]
		#decode needed- stop errors appearing
		#also, replace silly things like two-humped camel emojis...
		tweetText=row [2].decode('utf-8')
		tweetCoord1=row [3]
		tweetCoord2=row [4]
		single_tweet_data_array = [tweetURL, tweetTime, tweetText, tweetCoord1, tweetCoord2]
	
		#return all of these values in an array
		return single_tweet_data_array
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"


def add_placemarks_to_kml(single_tweet_data_array):
		try:
			tweetURL=single_tweet_data_array[0]
			tweetTime=single_tweet_data_array[1]
			tweetText=single_tweet_data_array[2]
			tweetCoord1=single_tweet_data_array[3]
			tweetCoord2=single_tweet_data_array[4]
		
			#add data to placemarks for kml
			placemark = ET.SubElement(doc, "Placemark")
			placemarkname = ET.SubElement(placemark, "name")
			placemarkname.text = tweetTime
			placemarkdesc = ET.SubElement(placemark, "description")
			placemarkdesc.text="Tweet: "+tweetText+".   Link to tweet: "+tweetURL
			placemarkstyleurl = ET.SubElement(placemark, "styleUrl")
			placemarkstyleurl.text="#additional_pin"
			placemarkpoint = ET.SubElement(placemark, "Point")
			coords = ET.SubElement(placemarkpoint, "coordinates")
			#silly coord error
			#swap them
			coords.text=tweetCoord2+", "+tweetCoord1+""+",0"

			#create file in a folder named kml_files within the same directory as the script
			ET.ElementTree(kmlDeclaration).write(newFileName, encoding="utf-8", xml_declaration=True)
			
		except Exception,e:
			print "+++ Something has gone wrong. "+str(e)+" +++"



   	
def main():
	try:
		print "***running the main method***"
		#generate timestamp
		generate_file_name()
		generate_kml_file()
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"
    


if __name__ == "__main__":
    main()
    	
