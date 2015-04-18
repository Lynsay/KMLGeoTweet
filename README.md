# KMLGeoTweet

Lynsay A. Shepherd, December 2014

## Overview
Twitter have unveiled a feature which allows users to download a <a href="https://blog.twitter.com/2012/your-twitter-archive">complete archive</a> of their own Twitter account.

This script reads in a CSV Twitter archive of tweets which contain geolocation information.  It then generates a KML file based on the information provided.  The KML file can be opened with Google Earth and provides an overview of places visited.

##Running This Script
First of all, you need to download your Twitter archive from <a href="http://www.twitter.com">Twitter</a>.  Unzip it.

Then run the following python script from within the main Twitter archive folder- <a href="https://github.com/Lynsay/Parse-Twitter-Archive">https://github.com/Lynsay/Parse-Twitter-Archive</a>.  This is a modified version of a script written by Michael E. Shea at <a href="http://mikeshea.net/">http://mikeshea.net/</a>.  You can find his original version at <a href="https://github.com/mshea/Parse-Twitter-Archive">https://github.com/mshea/Parse-Twitter-Archive</a>.  The script parses the archive and generates a CSV of tweets which contain geolocation information.

This script then converts the CSV file to KML, meaning it can be opened with Google Earth. Licensed Under the MIT License (MIT).
