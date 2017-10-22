import numpy as np
import operator
# data = file("../Dataset/cleanedArizona.csv")
# data = data.read()
# data = data.split('\n')

# lat=[]
# lng=[]
# a=0
# dct={}
# zipcode='85721'

# for i in data:
# 	tokens = i.split(',')
# 	if(tokens[4] == zipcode):
# 		dct['lat'] = np.float32(tokens[5])
# 		dct['lng'] = np.float32(tokens[6])
# 		lat.append(dct)
# print lat
def latAndLng(zipcode):
	data = file("../Dataset/cleanedArizona.csv")
	data = data.read()
	data = data.split('\n')

	lat1=[]
	lng1=[]
	dct_lat={}
	dct_lng={}
	lct=[]
	a=0

	for i in data:
		tokens = i.split(',')
		if(tokens[4] == zipcode):
			lat =(tokens[5])
			lng =(tokens[6])
			try:
				dct_lat[lat]=dct_lat[lat]+1
				dct_lng[lng]=dct_lng[lng]+1
			except:
				dct_lat[lat]=1
				dct_lng[lng]=1

	for k,v in dct_lat.items():
		lat1.append(np.float32(k))
	for k,v in dct_lng.items():
		lng1.append(np.float32(k))
	if len(lat1)>1000 and len(lng1)>1000:
		for i in range(999):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)>500 and len(lng1)>500:
		for i in range(499):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)>250 and len(lng1)>250:
		for i in range(249):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)>100 and len(lng1)>100:
		for i in range(99):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)>50 and len(lng1)>50:
		for i in range(49):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	elif len(lat1)<50 and len(lng1)<50:
		for i in range(len(lng1)-1):
			lct.append(lat1[i])
			lct.append(lng1[i+1])
	return lct

def monthDayHr():
	dct_zipProb = {'85755':0.5,'85704':0.1,'85718':0.9,'85719':0.4,'85745':0.23,'85756':0.778,'85706':0.46,'85712':0.41,'85748':0.76}
	zipAndProb = prob_zip_MClearning(dct_zipProb)
	print zipAndProb


def prob_zip_MClearning(dct_zipProb):
	sorted_dct = sorted(dct_zipProb.items(),key=operator.itemgetter(1))
	sorted_dct = dict(sorted_dct)
	all_lat_lng=[]
	for k,v in sorted_dct.items():
		all_lat_lng.append(latAndLng(k))
	lat_lng_top_three = [all_lat_lng[0],all_lat_lng[1], all_lat_lng[2],all_lat_lng[len(all_lat_lng)-3],all_lat_lng[len(all_lat_lng)-2],all_lat_lng[len(all_lat_lng)-1]]
	return lat_lng_top_three

monthDayHr()