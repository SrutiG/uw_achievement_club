import dstk
import requests
import json

dstk = dstk.DSTK()

def addressToLocation(address):
    address_info = {}
    try:
        results = dstk.street2coordinates(address)
        latitude = results[address]['latitude']
        longitude = results[address]['longitude']
        county_resp = requests.get('http://data.fcc.gov/api/block/find', params={'format':'json','latitude':latitude, 'longitude':longitude})
        county_info = json.loads(county_resp.content)
        address_info['county'] = county_info['County']['name']
        address_info['latitude'] = results[address]['latitude']
        address_info['longitude'] = results[address]['longitude']
    except Exception as e:
        print e
        raise ValueError("error geocoding location")
    return address_info