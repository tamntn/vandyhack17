from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json
import watson_developer_cloud 

app = Flask(__name__)


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
#print((context))
	

	# print(contexts)
	response = conversation.message({
	'workspace_id':'1d7276eb-2bff-4e67-b8fc-8261df022546',
	'message_input':{'text': message},	
    'context': context},
    new(response))
    



	account_sid = "ACc5173ddda5dea6f7c9b4398c0f80d545"
	auth_token  = "87e59826d7f49301f6bebedf32d21d51"

	client = Client(account_sid, auth_token)

	message1 = client.messages.create(
		to=number, 
		from_=twilioNumber,
		body="y no watson?")

	# def new(response):
	# 	print(response.output.text[0])
	# 	if context == None:
	# 		contexts.append({'from': number, 'context': response.context})
	# 	else:
	# 		contexts[contextIndex].context = response.context


	
	
if __name__ == "__main__":
    app.run(debug=True)