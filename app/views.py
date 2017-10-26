from app import app
from flask import render_template, request, redirect, session, url_for, jsonify
import os
import json

@app.route('/')
def index():
	return redirect('home')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/resources')
def resources():
	return render_template('resources.html')

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



