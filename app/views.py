from app import app
from flask import render_template, request, redirect, session, url_for, jsonify
import os
import json
import csv
from app import db, models
from utils import addressToLocation
from sqlalchemy import exc

@app.route('/')
def index():
	return redirect('home')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	success_stories = []
	with app.open_resource('success_stories.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			success_story = row['Success_Story']
			success_story = unicode(success_story, 'utf-8')
			row['Success_Story'] = success_story
			success_stories.append(row)
	goals = [{'name':'education', 'description':'A goal related to school, training programs, certificates, or other formal learning'}, {'name':'health', 'description': 'A goal related to improving general health, treating a specific disease, improving health awareness, etc.'}, {'name':'income', 'description':'Financial goals such as getting a new job, a better paying job, or building financial skills'}, {'name':'civic', 'description':'A goal related to politics, government, local organizations, etc.'}, {'name':'community', 'description':'A goal related to improving where you and your family live, joining a local club or organization, etc.'}]
	return render_template('about.html', goals=goals, success_stories=success_stories)

@app.route('/resources')
def resources():
	return render_template('resources.html')

@app.route('/county')
def county():
	return render_template('county.html', county='fulton')

@app.route('/locations')
def locations():
	with app.open_resource("static/js/ac_locations.json", "r") as data_file:
		for line in data_file:
			data_file = line.strip()
		data = data_file
	return jsonify(data = data)

@app.route('/mapstyles')
def mapstyles():
	data = ""
	with app.open_resource("static/js/styles.json", "r") as data_file:
		for line in data_file:
			data += line.strip()
	return jsonify(data = data)

@app.route('/administrator')
def administrator():
	if not session.get('admin_login'):
		return redirect('administrator/login')
	return redirect('administrator/home')

@app.route('/administrator/home')
def administrator_home():
	if not session.get('admin_login'):
		return redirect('administrator/login')
	success_stories = []

	with app.open_resource('success_stories.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			success_story = row['Success_Story']
			success_story = unicode(success_story, 'utf-8')
			row['Success_Story'] = success_story
			success_stories.append(row)
	return render_template('admin-dash/home.html', locations=locations, success_stories=success_stories)

@app.route('/administrator/login', methods=['GET','POST'])
def administrator_login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		query = models.Admin.query.filter_by(username=username).filter_by(password=password).all()
		if query != []:
			session['admin_login'] = True
			return redirect('administrator/home')
		else:
			return render_template('admin-dash/login.html', error=True)
	return render_template('admin-dash/login.html', error=False)

@app.route('/administrator/logout')
def administrator_logout():
	session['admin_login'] = False
	return redirect('administrator/login')

@app.route('/administrator/locations')
def administrator_locations():
	if not session.get('admin_login'):
		return redirect('administrator/login')
	locations = []
	locations_query = models.Location.query.all()
	for location in locations_query:
		locations.append(location.__dict__)
	return render_template('admin-dash/locations.html', locations=locations)

@app.route('/administrator/add_location', methods=['POST'])
def administrator_add_location():
	address = request.form['address']
	name = request.form['name']
	try:
		loc_vals = addressToLocation(address)
		county = loc_vals['county']
		latitude = loc_vals['latitude']
		longitude = loc_vals['longitude']
		db.session.add(models.Location(name=name, county=county, address=address, latitude=latitude, longitude=longitude))
		db.session.commit()
	except ValueError as e:
		print e
		return jsonify({"success":False,"message":"Error: invalid address '%s'"%(address), "status_code":400})
	except exc.IntegrityError as e:
		print e
		return jsonify({"success":False,"message":"Either address '%s' or location name '%s' already exists"%(address,name), "status_code":400})
	return jsonify({"success":True,"message":"successful geocode", "status_code":200})

@app.route('/administrator/delete_location', methods=['POST'])
def administrator_delete_location():
	name = request.form['name']
	delete_location = models.Location.query.get(name)
	db.session.delete(delete_location)
	db.session.commit()
	return jsonify({"success":True,"message":"successful delete", "status_code":200})

@app.route('/administrator/edit_location', methods=['POST'])
def administrator_edit_location():
	name = request.form['name']
	address = request.form['address']
	location = models.Location.query.get(name)
	address_loc = models.Location.query.filter_by(address=address).all()
	if location == None and address_loc == []:
		old_location_name = request.form['old-name']
		location = models.Location.query.get(old_location_name)
		try:
			loc_vals = addressToLocation(address)
			location.name = name
			location.address = address
			location.county = loc_vals['county']
			location.latitude = loc_vals['latitude']
			location.longitude = loc_vals['longitude']
			db.session.commit()
		except ValueError as e:
			print e
			return jsonify({"success":False,"message":"Error: invalid address '%s'"%(address), "status_code":400})
	elif location == None:
		location = address_loc[0]
		location.name = name
		db.session.commit()
	elif address_loc == []:
		try:
			loc_vals = addressToLocation(address)
			location.address = address
			location.county = loc_vals['county']
			location.latitude = loc_vals['latitude']
			location.longitude = loc_vals['longitude']
			db.session.commit()
		except ValueError as e:
			print e
			return jsonify({"success":False,"message":"Error: invalid address '%s'"%(address), "status_code":400})
	else:
		print "[Info] No location change"
		return jsonify({"success":True,"message":"location with address already exists, no change made", "status_code":200})
	return jsonify({"success":True,"message":"successful edit", "status_code":200})




