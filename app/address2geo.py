import dstk
import requests
import json

dstk = dstk.DSTK()
locations = [{"name": "Pebblebrook High School", "address": "991 Old Alabama Rd Sw Mableton, GA 30126"}, {"name": "Walton Reserve Apartments", "address": "7075 Walton Reserve Ln, Austell, GA 30168"}, {"name": "Cenacle Coffee shop", "address": "2844 Veterans Memorial Hwy SW, Austell, GA 30168"}, {"name": "Destiney World Church", "address": "7400 Factory Shoals Rd, Austell, GA 30168"}, {"name": "Lift Community Development Center", "address": "2300 Godby Rd, College Park, GA 30349"}, {"name": "Hearts to Nourish Hope", "address": "640 GA-138, Riverdale, GA 30274"}, {"name": "Kinship Care", "address": "849 Battle Creek Rd, Jonesboro, GA 30236"}, {"name": "Decatur cooperative Ministries", "address": "1523 Church St, Decatur, GA 30030"}, {"name": "Park Lane Elementary", "address": "2809 Blount St, East Point, GA 30344"}, {"name": "Harmony Leland Elementary","address": "5891 Dodgen Rd SW, Mableton, GA 30126"}, {"name": "MeadowCreek High School", "address": "4455 Steve Reynolds Blvd, Norcross, GA 30093"}, {"name": "MeadowCreek Elementary School", "address": "5025 Georgia Belle Ct, Norcross, GA 30093"}, {"name": "Sweetwater Mission", "address": "6289 Veterans Memorial Hwy #12a, Austell, GA 30168"}, {"name": "Perry Learning Center", "address": "137 Spring St, Jonesboro, GA 30236"}, {"name": "Spring Lake Apartments", "address": "100 Chase Common Dr, Norcross, GA 30071"}, {"name": "Willow Trail apartments", "address": "1500 Willow Trail Dr, Norcross, GA 30093"}, {"name": "Woodland Ridge", "address": "1355 Indian Trail Lilburn Rd NW, Norcross, GA 30093"}, {"name": "Yells, Inc.", "address": "779 Franklin Gateway SE, Marietta, GA 30067"}, {"name": "Action Ministries", "address": "1700 Century Cir NE Suite 200 Atlanta, GA 30345"}, {"name": "Zion Hill Community Development Center", "address": "2741 Bayard St, East Point, GA 30344"}]
for ind,location in enumerate(locations):
    results = dstk.street2coordinates(location['address'])
    latitude = results[location['address']]['latitude']
    longitude = results[location['address']]['longitude']
    county_resp = requests.get('http://data.fcc.gov/api/block/find', params={'format':'json','latitude':latitude, 'longitude':longitude})
    county_info = json.loads(county_resp.content)
    locations[ind]['county'] = county_info['County']['name']
    locations[ind]['latitude'] = results[location['address']]['latitude']
    locations[ind]['longitude'] = results[location['address']]['longitude']
print locations
