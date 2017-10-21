from flask import Flask, render_template, url_for, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)


@app.route("/")
def hello():
	
	return "hellow world"

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    resp.message("this is a reply")

    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)