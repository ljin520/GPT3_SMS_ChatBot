import mimetypes
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from openai_api import text_complition
from twilio_api import send_message
from dotenv import load_dotenv
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


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        message = request.values.get('Body').lower()
        # sender_id = request.values.get('From')
        
        # Get response from Openai
        # result = text_complition(message)
        result = {
            'status': 1,
            'response': "My information is coming"
        }
        
        if result['status'] == 1:
            resp = MessagingResponse()
            resp.message(result['response'])
            
            # send_message(sender_id, result['response'])
            return Response(str(resp), mimetype="application/xml")
    except:
        pass
        return None



if __name__ == "__main__":
    app.run(debug=True)