from app import app
from flask import render_template, request, redirect, session, url_for, jsonify
import os
import json
import csv

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
	if not session['admin_login']:
		return redirect('administrator/login')
	return redirect('administrator/home')

@app.route('/administrator/home')
def administrator_home():
	if not session.get('admin_login'):
		return redirect('administrator/login')
	success_stories = []
	with app.open_resource("static/js/ac_locations.json", "r") as data_file:
		for line in data_file:
			data_file = line.strip()
		locations = json.loads(data_file)
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
		if username == 'test' and password == 'test':
			session['admin_login'] = True
			return redirect('administrator/home')
	return render_template('admin-dash/login.html')




