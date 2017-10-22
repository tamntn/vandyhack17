#!/usr/bin/python
from flask import Flask, render_template, url_for,  request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json
import watson_developer_cloud 
import sys
from model_func import *
import csv
app = Flask(__name__)

ziploc={
"85701":"Tucson Convention Center, N. Granada Ave, S. Stone Ave, S. 6th Ave & S. 4th Ave",
"85704":"Casas Adobes (N. La Canada Dr, Tohono Chul Park, W. Magee Rd & W. Calle Concordia)",
"85705":"Flowing Wells, Limberlost & Amphi Areas",
"85706":"S. Nogales Hway, S. Campbell Ave & E. Benson Hway",
"85709":"University of Arizona campus & N. Commerce Park Loop ",
"85710":"E. Broadway Blvd & E. 22nd St around Panano Wash Trails",
"85711":"Poets Square, Highland Vista Cinco Via, Naylor & Myers Areas",
"85712":"Rillito, Old Fort Lowell, Glenn Heights, Tucson Botanical Gardens, Avondale & Harlan Heights",
"85713":"S. La Cholla Blvd, S. Mission Road, Santa Cruz River Park & Las Vistas",
"85715":"Tucson Country Club, Sunset North & Indian Ridge Estates",
"85716":"Central Tucson (N. Country Club Road, Palo Verde, El Conquistador)",
"85718":"Catalina Foothills and North Areas",
"85719":"Campus Farm, Mountain View, Samos, Campbell Grant, Catalina Vista & Jefferson Park",
"85721":"Central Campus - University of Arizona",
"85724":"University of Arizon - College of Medicine and Surrounding Medical Facilities",
"85745":"West Tucson Areas",
"85748":"East Tucson Areas",
"85755":"North Tucson Areas (Stone Canyon, Rancho Vistoso, Sunridge & Innovation Corporate Center)",
"85756":"South Tucson Areas & Tucson International Airport"
}

@app.route("/")
def hello():
	return render_template('dashboard.html')

@app.route("/locationPrediction")
def locationPrediction():
	return render_template('locationPrediction.html')

@app.route("/typePrediction")
def typePrediction():
	return render_template('typePrediction.html')

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

def redzone():
	redzones=["Weir","Library","Square","down town"]
	re=""
	for redzone in redzones:
		re=re+" \n"+redzone
	return re



contexts=[]
@app.route("/bot", methods=['GET','POST'])
def bot_talk():
	
	message=request.values.get('Body',None)
	number=request.values.get('From',None)
	twilioNumber = request.values.get('To')
	context=None
	index =0
	contextIndex=0
	for cont in contexts:
		print(cont.get("From",None))
		if cont.get("From",None)==number:
			context=cont.get("Body",None)
			contextIndex=index
		index=index+1
	print("Received Message from "+number+"saying " +message )
	
	conversation = watson_developer_cloud.ConversationV1(
   	 username='baa8a3a1-6dc1-4458-a23a-ce3115133ae2',
   	 password='MD42bUyTN2CE',
    	version='2017-05-26')
	
  
	response=conversation.message(workspace_id='1d7276eb-2bff-4e67-b8fc-8261df022546',
                             message_input={'text': message})
	print(json.dumps(response, indent=2))
	account_sid = "ACc5173ddda5dea6f7c9b4398c0f80d545"
	auth_token  = "87e59826d7f49301f6bebedf32d21d51"
	client = Client(account_sid, auth_token)

	try:
		def new(response):
			if context == None:
				contexts.append({'from': number, 'context': response.context})
			else:
				contexts[contextIndex].context = response.context
		reply =response["output"]["text"][0]
		try:
			e=response["entities"][0]["entity"]
		except:
			e=" "

		if response["intents"][0]['intent']=="Redzone" and e=="sys-date":
			apple =response["entities"][0]["value"]
			m=apple.split("-")[1]
			d=apple.split("-")[2]
			string=""
			zipvalues=prob_zip(m,d,"Friday")
			for _, zipcode in zip(range(3),zipvalues):
				string=string+(ziploc[zipcode])+"\n Prob "+str(zipvalues[zipcode])+" \n"
			apple="I have listed 3 danger zone: "+string
		else:	
			apple=response["output"]["text"][0]
	
		message1 = client.messages.create(
		to=number, 
		from_=twilioNumber,
		body=apple)
	except:
		message1 = client.messages.create(
		to=number, 
		from_=twilioNumber,
		body="I am learning.")
	# new(response)
	
if __name__ == '__main__':
    app.run()