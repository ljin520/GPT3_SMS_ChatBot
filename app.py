from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from mybot import ask, append_interaction_to_chat_log
from twilio.rest import Client
import os


# app = Flask(__name__)
# # if for some reason your conversation with the bot gets weird, change the secret key 
# app.config['SECRET_KEY'] = '89djhff9lhkd93'

# account_sid = os.getenv('TWILIO_ACCOUNT_SID')
# auth_token = os.getenv('TWILIO_AUTH_TOKEN')


# @app.route('/')
# def home():
#     return 'All is well...'

# @app.route('/mybot', methods=['POST'])
# async def mybot():
#     try:
#         question = request.form['Body']
#         sender_id = request.form['From']
        
#         answer = ask(question, None)
#         # session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
#                                                       # chat_log)
#         if answer['status'] == 1:
#             client = Client(account_sid, auth_token)
#             client.messages.create(
#                 from_=os.getenv('FROM'),
#                 body=answer['response'],
#                 to=sender_id,
#             )
        
#     except:
#         pass
#     return "OK",200



from openai_api import text_complition
from twilio_api import send_message


from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/mybot', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        # Get response from Openai
        result = text_complition(message)
        if result['status'] == 1:
            send_message(sender_id, result['response'])
    except:
        pass
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)