# vandyhack17

## Inspiration
With college campus' increased focus on student safety in recent years, we desired to analyze crime rates in notable college towns.

## Features
The web application uses a feed-forward neural network to predict, given a specific month, day of week, and time, the probability of a crime occuring for all the major ZIP codes of the town. These probabilities are then visualized via a heat map. A similar neural network calculates the probability for different probabilities of crime. Additionally, other interesting crime statistics calculated via conventional methods are provided. The user can interface with the application via either a traditional web-app or an SMS chatbot.

## Technologies 
The application's neural networks were implemented using Microsoft Cognitive Toolkit (CNTK). Google's Maps API along with its Geocoding API are used to display the heat map. Tulio provides the SMS user interface while the actual chatbot is powered by IBM's Watson. R was used to provide additional statistics of interest.

## Challenges
Finding a large, quality data set was the difficult; even the best data set found, one for Tucson, AZ, was missing many ZIP codes. This required using latitude and longitude data in the file along with Google's Geocoding API to determine the missing ZIP codes. While the machine learning model proved to be most accurate in predicting the ZIP codes for crimes, the same could not be said for its predictions of crime types. This is likely due to the many different categories of crime in the data set and the difficulty of traing a classification model with so many probabilities to calculate.

Using Tulio to provide the SMS user interface was arguably the most unique and new challenge for the team.

Additionally, deploying the web project's many different parts and integrating them proved to be most challenging.

## Accomplishments
When evaluated on the test portion of the data set, the machine learning model achieved an approximately 80% accuracy in choosing the ZIP code where a crime occured. As for the application itself, the ability to use the application via both the browser and SMS makes for an excellent user interface.o

## Lessons
Though the team had experience training machine learning models, deploying one as part of an application was a new challenge. The team gained significant experience with the technologies mentioned and learned how to combine data science and web development talent.

## Future Plans
The current application employs a dataset on crime statistics in Tucson, AZ, but there are excellent data sets for other university towns as well, such as Baton Rouge, LA and College Park, MA. Additionally, to obtain better predictions on type of crime, the data sets for multiple universities could be combined (in contrast to the ZIP code model, which depends specifically on location).
