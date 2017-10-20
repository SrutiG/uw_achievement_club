from app import app
from flask import render_template, request, redirect, session
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



