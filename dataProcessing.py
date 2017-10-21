import csv
import datetime
from pprint import pprint
from urllib2 import Request, urlopen, URLError
import requests
import json

filename = "originalArizona.csv"
newfile = "cleanedArizona.csv"
inputData = []

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def getZipFromLatLong(lat, lon):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + lon + "&result_type=street_address&key=AIzaSyBcIGXEd-1-6ZrqjN_ZpN-0IiM5_VNovX4"
    request = Request(url)
    try:
        response = urlopen(request)
        data = response.read()
    except URLError, e:
        print 'No address found.', e
        return ""

    parsed_json = json.loads(data)
    if(parsed_json['results'] == []):
        print "Your lat/long is invalid."
        return ""
    else:
        #firstResult = (parsed_json['results'][0]['address_components'][6]['long_name'])
        firstResult = (parsed_json['results'][0]['address_components'])
        for x in range(0, len(firstResult)):
            if firstResult[x]["types"] == [ "postal_code" ]:
                return str(firstResult[x]["long_name"])

with open(newfile, 'a') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    with open(filename, 'rb') as csv_data:
        reader = csv.reader(csv_data)
        header = reader.next()
        rows = [row for row in reader if row]
        print len(rows)
        count = 0
        for row in rows:
            year = row[0]
            month = row[1]
            hour = row[2]
            day = row[3]
            latitude = row[6]
            longtitude = row[7]
            if row[5] == "null" or len(row[5]) == 0:
                zipCode = getZipFromLatLong(latitude, longtitude)
            else:
                zipCode = row[5]
            crimeType = row[8]
            inputRow = [year, month, hour, day, zipCode, latitude, longtitude, crimeType]
            if(zipCode!=""):
                spamwriter.writerow(inputRow)
            count += 1
            print count

#with open(newfile, 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=',',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    for row in inputData:
#        spamwriter.writerow(row)
        

