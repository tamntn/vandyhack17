from flask import Flask, render_template, url_for, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)


@app.route("/")
def hello():
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('crime_foretell.html', result=data)

@app.route('/maps')
def maps(data=None):
	data = {"lat": 37.775, "lng": -56.434}
	return render_template('maps.html',result=data)

@app.route('/test')
def test(data=None):
	data = {"lat": 37.775, "lng": -122.434}
	return render_template('test.html',result=json.dumps(data))

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