from app import app
from flask import render_template, request, redirect, session
import os
import json

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'
