import cntk as C
import numpy as np

C.use_default_device()

model_prefixes = ["arizona"]
dictDir = ""
modelDir = ""
numType = np.float32

def loadDict(path):
    dictionary = {}
    with open(path, "r") as categories:
        i = 0
        for line in categories.readlines():
            line = line.strip()
            if line and (line not in dictionary):
               dictionary[line] = i
               i += 1 
    return dictionary

dictNames = ["month", "hours", "weekdays", "zips", "crimes"]
dictPaths = [dictDir + model_prefixes[0] + "_" + dictName + "_dict" for dictName in dictNames]

monthsDict = loadDict(dictPaths[0])
hoursDict = loadDict(dictPaths[1])
weekdaysDict = loadDict(dictPaths[2]) 
zipsDict = loadDict(dictPaths[3])
crimesDict = loadDict(dictPaths[4])

features = C.input_variable(len(monthsDict) + len(hoursDict) + len(weekdaysDict), dtype = numType)
#zip_labels = C.input_variable(len(zipsDict))
#crime_labels = C.input_variable(len(crimesDict))

zip_model = C.Function.load(modelDir + model_prefixes[0] + "_zips.cmf")
crime_model = C.Function.load(modelDir + model_prefixes[0] + "_crimes.cmf")

#print(zip_model)
#print(crime_model)

def toOneHot(category, indexDict):
    oneHot = np.zeros((len(indexDict)), dtype = numType)
    oneHot[ indexDict[category] ] = 1
    return oneHot 


def fromOneHot(oneHot, indexDict):
    index = np.argmax(oneHot)
    for key, value in indexDict.items():
        if value == index: return key

    return None    

#print(fromOneHot(toOneHot("Wednesday", weekdaysDict), weekdaysDict))

def convertInputs(month, hour, day):
    month = toOneHot(month, monthsDict)
    hour = toOneHot(hour, hoursDict)
    day = toOneHot(day, weekdaysDict)

    return np.concatenate( (month, hour, day) )

converted = convertInputs("7", "3", "Wednesday")
#print(converted)
#print(converted[:12])
#print(converted[12: 12 + 24])
#print(converted[12 + 24: 12 + 24 + 7])



def eval_zip(month, hour, day, model_prefix = model_prefixes[0]):
    input_var = convertInputs(month, hour, day)
    #print(input_var)
    #print(len(input_var))
    oneHot = zip_model.eval({zip_model.arguments[0] : input_var})
    label = fromOneHot(oneHot, zipsDict)
    return label



def eval_crime(month, hour, day, model_prefix = model_prefixes[0]):
    input = convertInputs(month, hour, day)
    oneHot = crime_model.eval({crime_model.arguments[0] : input})
    label = fromOneHot(oneHot, crimesDict)
    return label

def eval_both(month, hour, day, model_prefix = model_prefixes[0]):
    return eval_zip(month, hour, day, model_prefix = model_prefix), eval_crime(month, hour, day, model_prefix = model_prefix)

zip_code, crime = eval_both("7", "3", "Wednesday")
print(zip_code)
print(crime)
