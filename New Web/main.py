from flask import Flask, render_template, url_for
import json

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()