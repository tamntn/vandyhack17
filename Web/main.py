from flask import Flask, render_template, url_for, request
#from twilio.twiml.messaging_response import MessagingResponse


import json
import numpy as np
import operator
# from application.app.folder.file import prob_zip, prob_crime, prob_both
# import sys
# sys.path.insert(0,'/path/to/model/'))

app = Flask(__name__)


@app.route("/")
def hello():
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('index.html', result=data)

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

def latAndLng(zipcode):
	data = file("../Dataset/cleanedArizona.csv")
	data = data.read()
	data = data.split('\n')

	lat1=[]
	lng1=[]
	dct_lat={}
	dct_lng={}
	lct=[]
	a=0

	for i in data:
		tokens = i.split(',')
		if(tokens[4] == zipcode):
			lat =(tokens[5])
			lng =(tokens[6])
			try:
				dct_lat[lat]=dct_lat[lat]+1
				dct_lng[lng]=dct_lng[lng]+1
			except:
				dct_lat[lat]=1
				dct_lng[lng]=1

	for k,v in dct_lat.items():
		lat1.append(np.float32(k))
	for k,v in dct_lng.items():
		lng1.append(np.float32(k))
	if len(lat1)>1000 and len(lng1)>1000:
		for i in range(999):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)>500 and len(lng1)>500:
		for i in range(499):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)>250 and len(lng1)>250:
		for i in range(249):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)>100 and len(lng1)>100:
		for i in range(99):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)<100 and len(lng1)<100:
		for i in range(49):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	return lct

def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    resp.message("this is a reply")

    return str(resp)


@app.route("/month_day_hour",methods=['POST','GET'])
def monthDayHr():
	if request.method == "POST":
		month = request.form['month']
		day = request.form['day']
		hour = request.form['hour']
	dct_zipProb = prob_zip(month,hour,day)
	zipAndProb = prob_zip_MClearning(dct_zipProb)
	return render_template('mdh.html',zipcode=zipAndProb)

def prob_zip_MClearning(dct_zipProb):
	sorted_dct = sorted(dct_zipProb.items(),key=operator.itemgetter(1))
	sorted_dct = dict(sorted_dct)
	all_lat_lng=[]
	for k,v in sorted_dct.items():
		all_lat_lng.append(latAndLng(k))
	lat_lng_top_three = [all_lat_lng[0],all_lat_lng[1], all_lat_lng[2],all_lat_lng[len(all_lat_lng)-3],all_lat_lng[len(all_lat_lng)-2],all_lat_lng[len(all_lat_lng)-1]]
	return lat_lng_top_three

if __name__ == "__main__":
    app.run(debug=True)
