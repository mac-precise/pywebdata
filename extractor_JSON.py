#!/usr/bin/python
# Data Extractor & Parser for JSON google maps API

import urllib.parse
import urllib.request
import urllib.error
import sys, json
#import requests

#Google maps url with JSON geocodes API
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#Read file name "api_key" with google api key. (https://developers.google.com/maps/documentation/geocoding/get-api-key)
keyFile = open('google_maps_api_key', 'r')
api_key = keyFile.readline()
keyFile.close()
key = '&key='+ api_key +'&callback=initialize'

#Get location data based on input entered location
while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address}) + key
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    #js = json.loads(str(data))
    print ('Retrieved data:',data)

#Write JSON data into local file named: "geo_data_file"
    with open("geo_data_file", "w") as write_file:
        json.dump(data.decode("utf-8"), write_file)
    js = {}

    try: js = json.loads(str(data.decode("utf-8")))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('Failure to retrieve')
        print (data)
        continue

    print (json.dumps(js, indent=4))

    latitude = js["results"][0]["geometry"]["location"]["lat"]
    longitude = js["results"][0]["geometry"]["location"]["lng"]
    print ('latitude',latitude,'longitude',longitude)
    location = js['results'][0]['formatted_address']
    print (location)
