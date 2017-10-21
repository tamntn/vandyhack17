from flask import Flask, render_template, url_for, request
import json
import numpy as np

app = Flask(__name__)


@app.route("/")
def hello():
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('crime_foretell.html', result=data)

@app.route("/test",methods=['POST','GET'])
def results():
	if request.method == 'POST':
		key = request.form['zipcode']
	lat = latAndLng(key)
	return render_template('test.html',zipcode=lat)

@app.route('/maps')
def maps(data=None):
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('maps.html',result=data)

# @app.route('/test')
# def test(data=None):
# 	data = {"lat": 37.775, "lng": -122.434}
# 	return render_template('test.html',result=json.dumps(data))

def latAndLng(zipcode):
	data = file("../Dataset/cleanedArizona.csv")
	data = data.read()
	data = data.split('\n')

	lat=[]
	dct={}

	for i in data:
		tokens = i.split(',')
		if(tokens[4] == zipcode):
			dct['lat'] = np.float32(tokens[5])
			dct['lng'] = np.float32(tokens[6])
			lat.append(dct)
	return lat
