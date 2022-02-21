#!/usr/bin/env python
# coding: utf-8


# Enter API KEY
api_key = "Your API KEY"

# import modules
import requests
from urllib.parse import urlencode


data_type = 'json'
endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
params = {"address": "1600 Ritchie Court,Rochelle,IL 61068", "key": api_key}
url_params = urlencode(params)

url = f"{endpoint}?{url_params}"
print(url)


def extract_lat_lng(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    # print(url)
    r = requests.get(url)
    # print('results:', r.json())

    if r.status_code not in range(200, 299): 
        return None
    
    if r.json()['results'] != []:
        return r.json()['results'][0]
    else:
        return None
    
    
# test a raw address
extract_lat_lng("9 Vose Farm Rd.,Peterborough,NH 03458")


# install pandas (in jupyter notebook, using pip if in terminal)
!pip install pandas
import pandas as pd

# import data
df = pd.read_excel("example_data.xlsx")
df

# Create list to save data
#Lat
lats = []
# Log
logs = []
# Type
types = []
# Data
temps = []
# Formatted Data
formadd = []

# Write a for loop to get Latitude, Longitude, formatted address or other attributes from GoogleMap
for i,row in enumerate(df.values):
    address = row[1]
    
    data = extract_lat_lng(address)
    if data !=None:
        lat = data['geometry']['location']['lat']
        lng = data['geometry']['location']['lng']
        location_type = data['geometry']['location_type']
        formatted_address = data['formatted_address']
    else:
        lat=None
        lng=None
        location_type=None
        formatted_address=None

    # put data in list
    lats.append(lat)
    logs.append(lng)
    formadd.append(formatted_address)
    types.append(location_type)

# add to datagrame
df['lat'] = lats
df['lng'] = logs
df['formatted_adress'] = formadd
df['location_type'] = types

# print and save data to xlsx format
print(df)
df.to_excel("Final_data.xlsx")
