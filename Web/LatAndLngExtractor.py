import numpy as np

data = file("../Dataset/cleanedArizona.csv")
data = data.read()
data = data.split('\n')

lat=[]
lng=[]
a=0
dct={}
zipcode='85721'

for i in data:
	tokens = i.split(',')
	if(tokens[4] == zipcode):
		dct['lat'] = np.float32(tokens[5])
		dct['lng'] = np.float32(tokens[6])
		lat.append(dct)
print lat
