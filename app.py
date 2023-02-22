import mimetypes
import os
from flask import Flask, Response, request,session
from twilio.twiml.messaging_response import MessagingResponse
from openai_api import text_complition
from twilio_api import send_message
from dotenv import load_dotenv
from twilio.rest import Client
from mybot import ask, append_interaction_to_chat_log

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

@app.route('/sms', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')

    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)

    r = MessagingResponse()
    r.message(answer)
    return str(r)


@app.route("/sms1", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body').lower()
    
    
    resp = MessagingResponse()
    
    if body == 'yes':
        resp.message("We are glad you enjoyed Drip2Duong Coffee!")
    elif body == 'no':
        resp.message("We are sorry to here that.")
    else:
        result = text_complition(body)
        resp.message(result['response'])
        # reszzp.message("Please respond to Drip2Duong with yes or no. If you wish to unsubscribe text stop")

    return Response(str(resp), mimetype="application/xml")

@app.route('/')
def home():
    return 'All is well...'


@app.route('/bot', methods=['GET','POST'])
def receiveMessage():
        message = request.values.get('Body').lower()
        
        # Get response from Openai
        result = text_complition(message)
        # result =  message + ": My information is coming"
        resp = MessagingResponse()
        resp.message(result)
        return Response(str(resp), mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)