from flask import Flask, render_template, url_for, request
import json
from model_func import *
import operator
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('dashboard.html')

@app.route("/locationPrediction")
@app.route("/locationPrediction", methods=['POST', 'GET'])
def locationPrediction():
	if request.method == 'POST':
		month = request.form['month']
		time = request.form['time']
		day = request.form['day']
		dct_zipProb = prob_zip(month, time, day)
		zipAndProb = prob_zip_MClearning(dct_zipProb)
		print zipAndProb
		return render_template('locationPrediction.html', data=zipAndProb)
	else:
		now = datetime.datetime.now()
		month = str(now.month)
		time = str(now.hour)
		day = datetime.datetime.today().weekday()
		if day==0:
			day = "Monday"
		elif day==1:
			day = "Tuesday"
		elif day==2:
			day = "Wednesday"
		elif day==3:
			day = "Thursday"
		elif day==4:
			day = "Friday"
		elif day==5:
			day = "Saturday"
		else:
			day = "Sunday"
		dct_zipProb = prob_zip(month, time, day)
		zipAndProb = prob_zip_MClearning(dct_zipProb)
		print zipAndProb
		return render_template('locationPrediction.html', data=zipAndProb)

def prob_zip_MClearning(dct_zipProb):
	sorted_dct = sorted(dct_zipProb.items(), key=operator.itemgetter(1))
	sorted_dct = dict(sorted_dct)
	all_lat_lng = []
	for k,v in sorted_dct.items():
		all_lat_lng.append(k)
		all_lat_lng.append(np.float32(v))
	return all_lat_lng

def prob_zip_MClearning2(dct_zipProb):
	sorted_dct = sorted(dct_zipProb.items(), key=operator.itemgetter(1))
	sorted_dct = dict(sorted_dct)
	all_lat_lng = []
	for k,v in sorted_dct.items():
		all_lat_lng.append(str(k))
		all_lat_lng.append(str(v))
	return all_lat_lng

@app.route("/typePrediction")
@app.route("/typePrediction", methods=['POST', 'GET'])
def typePrediction():
	if request.method == 'POST':
		month = request.form['month']
		time = request.form['time']
		day = request.form['day']
		dct_zipProb = prob_crime(month, time, day)
		zipAndProb = prob_zip_MClearning2(dct_zipProb)
		print dct_zipProb
		return render_template('typePrediction.html', data=zipAndProb)
	else:
		now = datetime.datetime.now()
		month = str(now.month)
		time = str(now.hour)
		day = datetime.datetime.today().weekday()
		if day == 0:
			day = "Monday"
		elif day == 1:
			day = "Tuesday"
		elif day == 2:
			day = "Wednesday"
		elif day == 3:
			day = "Thursday"
		elif day == 4:
			day = "Friday"
		elif day == 5:
			day = "Saturday"
		else:
			day = "Sunday"
		dct_zipProb = prob_crime(month, time, day)
		zipAndProb = prob_zip_MClearning2(dct_zipProb)
		print zipAndProb
		return render_template('typePrediction.html', data=zipAndProb)

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route('/showMaps')
def showMaps(data=None):
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('maps.html',result=data)

@app.route('/test')
def test(data=None):
	data = {"lat": 37.775, "lng": -122.434}
	return render_template('test.html',result=json.dumps(data))



######################### Old Menu Sidebar #######################

@app.route("/icons")
def icons():
	return render_template('archive/icons.html')

@app.route("/maps")
def maps():
	return render_template('maps.html')

@app.route("/notifications")
def notifications():
	return render_template('archive/notifications.html')

@app.route("/table")
def table():
	return render_template('archive/table.html')

@app.route("/typography")
def typography():
	return render_template('archive/typography.html')

@app.route("/user")
def user():
	return render_template('archive/user.html')

if __name__ == '__main__':
    app.run()