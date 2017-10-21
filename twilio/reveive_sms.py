from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from watson_developer_cloud import ConversationV1


app = Flask(__name__)


conversation = ConversationV1(
  username = 'baa8a3a1-6dc1-4458-a23a-ce3115133ae2',
  password = 'MD42bUyTN2CE',
  version = '{2017-05-26}'
)
workspace_id = '1d7276eb-2bff-4e67-b8fc-8261df022546'



@app.route("",methods)
def index()
	return("Hello World")

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

