import numpy as np

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

num_features = len(monthsDict) + len(hoursDict) + len(weekdaysDict)
num_zips = len(zipsDict)
num_crimes = len(crimesDict)

def softmax(array):
    return np.exp(array) / sum(np.exp(array))

#Extract weights and biases written to text from CNTK script
def parameters(path, num_features, num_classes):
    weights = np.ndarray( (num_features, num_classes), dtype = numType )
    biases = np.ndarray( (num_classes), dtype = numType )

    with open(path, "r") as params:
        i = 0
        j = 0
        for k in range(num_features * num_classes):
            weight = params.readline().strip()
            weights[i][j] = weight
            j += 1
            if j == num_classes:
                j = 0
                i += 1

        for k in range(num_classes):
            bias = params.readline().strip()
            biases[k] = bias

    return weights, biases


zip_weights, zip_biases = parameters("zips.param", num_features, num_zips)
crime_weights, crime_biases = parameters("crimes.param", num_features, num_crimes)


def toOneHot(category, indexDict):
    oneHot = np.zeros((len(indexDict)), dtype = numType)
    oneHot[ indexDict[category] ] = 1
    return oneHot 


def fromProbs(oneHot, indexDict):
    index = np.argmax(oneHot)
    for key, value in indexDict.items():
        if value == index: return key

    return None    


def convertInputs(month, hour, day):
    month = toOneHot(month, monthsDict)
    hour = toOneHot(hour, hoursDict)
    day = toOneHot(day, weekdaysDict)

    return np.concatenate( (month, hour, day) )


def applyParameters(features, weights, biases):
    product = np.dot( np.transpose(weights), features ) 
    return product + biases


def prob_zip_helper(month, hour, day, model_prefix = model_prefixes[0]):
    input_var = convertInputs(month, hour, day)
    probs = applyParameters(input_var, zip_weights, zip_biases)
    return softmax(probs)

def prob_crime_helper(month, hour, day, model_prefix = model_prefixes[0]):
    input_var = convertInputs(month, hour, day)
    probs = applyParameters(input_var, crime_weights, crime_biases)
    return softmax(probs)


def sortedByValue(probs, dictionary):
    probDict = {}
    categories = sorted(dictionary, key = dictionary.get)

    for category in categories:
        #print("category =", category)
        index = dictionary[category]
        #print("index =", index)
        probability = probs[ index ]
        #print("probability =", probability)
        probDict[category] = probability

    return probDict

##########################PUBLIC INTERFACE#######################################

def prob_zip(month, hour, day, model_prefix = model_prefixes[0]):
    probs = prob_zip_helper(month, hour, day, model_prefix = model_prefix)
    return sortedByValue(probs, zipsDict)

    #return np.ndarray.tolist(prob_zip_helper(month, hour, day, model_prefix = model_prefix))[0]

def prob_crime(month, hour, day, model_prefix = model_prefixes[0]):
    probs = prob_crime_helper(month, hour, day, model_prefix = model_prefix)
    return sortedByValue(probs, crimesDict)

    #return np.ndarray.tolist(prob_crime_helper(month, hour, day, model_prefix = model_prefix))[0]

def prob_both(month, hour, day, model_prefix = model_prefixes[0]):
    return prob_zip(month, hour, day, model_prefix = model_prefix), prob_crime(month, hour, day, model_prefix = model_prefix)


"""
def eval_zip(month, hour, day, model_prefix = model_prefixes[0]):
    probs = prob_zip_helper(month, hour, day, model_prefix = model_prefix)
    label = fromProbs(probs, zipsDict)
    return label
def eval_crime(month, hour, day, model_prefix = model_prefixes[0]):
    probs = prob_crime_helper(month, hour, day, model_prefix = model_prefix)
    label = fromProbs(probs, crimesDict)
    return label
def eval_both(month, hour, day, model_prefix = model_prefixes[0]):
    return eval_zip(month, hour, day, model_prefix = model_prefix), eval_crime(month, hour, day, model_prefix = model_prefix)
"""
#print(prob_zip("2","2","Sunday"))