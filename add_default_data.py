import json
from app import db,models

# add test admins
db.session.add(models.Admin(username='srutig', email='sruti@gatech.edu', password='pass'))
db.session.commit()
db.session.add(models.Admin(username='test', email='test@uw.org', password='test'))
db.session.commit()
# add locations
locations = json.load(open('app/static/js/ac_locations.json'))
for location in locations:
    db.session.add(models.Location(name=location['name'], county=location['county'], address=location['address'], latitude=location['latitude'], longitude=location['longitude']))
    db.session.commit()
# add success stories