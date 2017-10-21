import jiphy

str="var express = require('express');var ConversationV1 = require('watson-developer-cloud/conversation/v1');var app = express();var contexts = [];"
jiphy.to.python(str)