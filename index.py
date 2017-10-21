
var express = require('express')
var ConversationV1 = require('watson-developer-cloud/conversation/v1')

var app = express()

var contexts = []

app.get('/smssent', def (req, res):
  var message = req.query.Body
  var number = req.query.From
  var twilioNumber = req.query.To

  var context = None
  var index = 0
  var contextIndex = 0
  contexts.forEach(def(value):
    print(value.from)
    if value.from == number:
      context = value.context
      contextIndex = index

    index = index + 1
  )

  print('Recieved message from ' + number + ' saying \'' + message  + '\'')

  var conversation = new ConversationV1({
    username: '0f4b2e6e-981b-4d08-89b6-25767cf57c02',
    password: '0f4b2e6e-981b-4d08-89b6-25767cf57c02',
    version_date: ConversationV1.VERSION_DATE_2016_09_20
  })

  print(JSON.stringify(context))
  print(contexts.length)

  conversation.message({
    input: { text: message },
    workspace_id: '',
    context: context
   }, def(err, response):
       if err:
         console.error(err)
       else:
         print(response.output.text[0])
         if context == None:
           contexts.append({'from': number, 'context': response.context})
         else:
           contexts[contextIndex].context = response.context


         var intent = response.intents[0].intent
         print(intent)
         if intent == "done":
           //contexts.splice(contexts.indexOf({'from': number, 'context': response.context}),1)
           contexts.splice(contextIndex,1)
           # Call REST API here (order pizza, etc.)


         var client = require('twilio')(
           'ACc5173ddda5dea6f7c9b4398c0f80d545',
           '87e59826d7f49301f6bebedf32d21d51'
         )

         client.messages.create({
           from: twilioNumber,
           to: number,
           body: response.output.text[0]
         }, def(err, message):
           if(err:
             console.error(err.message)

         })

  })

  res.send('')
)

app.listen(3000, def ():
  print('Example app listening on port 3000!')
);
