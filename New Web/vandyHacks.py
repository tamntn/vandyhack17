from flask import Flask, render_template, url_for,  request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json

app = Flask(__name__)


@app.route("/")
def hello():
	return render_template('dashboard.html')

@app.route("/icons")
def icons():
	return render_template('icons.html')

@app.route("/maps")
def maps():
	return render_template('maps.html')

@app.route("/notifications")
def notifications():
	return render_template('notifications.html')

@app.route("/table")
def table():
	return render_template('table.html')

@app.route("/template")
def template():
	return render_template('template.html')

@app.route("/typography")
def typography():
	return render_template('typography.html')

@app.route("/user")
def user():
	return render_template('user.html')

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

def redzone():
	redzone=["Weir","Library","Square","down town"]
	return redzone

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


	account_sid = "ACc5173ddda5dea6f7c9b4398c0f80d545"
	auth_token  = "87e59826d7f49301f6bebedf32d21d51"

	client = Client(account_sid, auth_token)
	try:
		
		
		def new(response):
			
				#resp=
			if context == None:
				contexts.append({'from': number, 'context': response.context})
			else:
				contexts[contextIndex].context = response.context
		if response["intents"][0]['intent']=="Redzone":
			apple =str(redzone())
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
		body="I dont understand")
	# new(response)
	
if __name__ == '__main__':
    app.run()