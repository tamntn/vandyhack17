## Crime ML Model
### Dependencies
* [CNTK 2.2](https://docs.microsoft.com/en-us/cognitive-toolkit/setup-windows-python?tabs=cntkpy22)
* [numpy](https://docs.scipy.org/doc/numpy-1.13.0/user/install.html)

### Functions
prob\_zip: Returns a str-to-float dictionary where the strings are ZIP codes and the floats are mutually exclusive probabilities for crime

prob\_crime: Returns a str-to-float dictionary where the strings are types of crime and the floats are mutually exclusive probabilities for such crimes

prob\_both: Returns a tuple of the results of prob\_zip and prob\_crime

#### Calling Functions
Call any given function f in the module like so: f(month, hour, day)

