#!/usr/bin/python
# Data Extractor & Parser for XML google maps API
# source code in Python 3

import urllib
import urllib.parse
import urllib.request
import urllib.error
import sys, json
#Warning The xml.etree.ElementTree module is not secure against maliciously constructed data. If you need to parse untrusted or unauthenticated data see XML vulnerabilities (https://docs.python.org/3/library/xml.html#xml-vulnerabilities)
import xml.etree.ElementTree as ETree

#Google maps url with XML geocodes API
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

#Read file name "api_key" with google api key. (https://developers.google.com/maps/documentation/geocoding/get-api-key)
keyFile = open('google_maps_api_key', 'r')
api_key = keyFile.readline()
keyFile.close()
key = '&key='+ api_key +'&callback=initialize'

#Get location data based on input entered location
while True:
    address = input('Enter location (or hit [Enter] to exit): ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address}) + key
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    print ('Retrieved data:',data)
    tree = ETree.fromstring(data)

    results = tree.findall('result')
    latitude = results[0].find('geometry').find('location').find('lat').text
    longitude = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text
    print ('latitude',latitude,'longitude',longitude)
    print (location)
