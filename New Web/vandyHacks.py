from flask import Flask, render_template, url_for
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

if __name__ == '__main__':
    app.run()