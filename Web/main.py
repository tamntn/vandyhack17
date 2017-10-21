from flask import Flask, render_template, url_for
import json

app = Flask(__name__)


@app.route("/")
def hello():
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('index.html', result=data)

@app.route('/maps')
def maps(data=None):
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('maps.html',result=data)

@app.route('/test')
def test(data=None):
	data = {"lat": 37.775, "lng": -122.434}
	return render_template('test.html',result=json.dumps(data))