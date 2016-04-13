 # -*- coding: utf-8 -*-
"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os, psycopg2, json, geojson
from flask import Flask, render_template, request, redirect, url_for, g, jsonify
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#metadata = MetaData()
#engine = create_engine('postgresql://atwysxmipzslwq:7EYnTdhVE5xzNBZwNv-CwVS8B-@ec2-54-163-228-188.compute-1.amazonaws.com/d66rq523l00c53')

#countries_table = Table('countries', metadata,
#    Column('gid', Integer, primary_key=True),
#    Column('admin',String),
#    Column('geom',Geometry('POLYGON'))
#)

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home """
    return render_template('home.html')

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
