import mimetypes
import os
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from openai_api import text_complition
from twilio_api import send_message
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body').lower()

    resp = MessagingResponse()
    
    if body == 'yes':
        resp.message("We are glad you enjoyed Drip2Duong Coffee!")
    elif body == 'no':
        resp.message("We are sorry to here that.")
    else:
        resp.message(body)
        # resp.message("Please respond to Drip2Duong with yes or no. If you wish to unsubscribe text stop")

    return Response(str(resp), mimetype="application/xml")

@app.route('/')
def home():
    return 'All is well...'


@app.route('/bot', methods=['GET','POST'])
def receiveMessage():
    try:
        message = request.values.get('Body').lower()
        # sender_id = request.values.get('From')
        
        # Get response from Openai
        # result = text_complition(message)
        result =  message + ": My information is coming"
        
        resp = MessagingResponse()
        resp.message(result)
        
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)    
            # send_message(sender_id, result['response'])
        message = client.messages.create(
            body='result',
            from_=os.getenv('FROM'),
            to='+9293796266'
        )
        return Response(str(resp), mimetype="application/xml")
    except:
        pass
        return Response(str("101"), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)