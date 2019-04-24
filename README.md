Py Web Data
===========

Couple of scripts for parsing XML/JSON based on extracted data from Geo Maps Google API.
Added MySQL connector script and DB data creator script as an examples to store and query collected data.

Requirements
------------

Script extractor_JSON.py and extractor_XML.py must have file named "google_maps_api_key" with proper Geo Maps Google API key.
If you do not have Geo Maps Google API key then you have to generate it here first: https://developers.google.com/maps/documentation/geocoding/get-api-key then put into "google_maps_api_key" file.

Tested on Python version 3.7.2

Installation
------------

Download and run:
$ python3 extractor_JSON.py
$ python3 extractor_XML.py
$ python3 mysql_connector.py
$ python3 mysql_db_data_creator.py
