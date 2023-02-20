from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from mybot import ask, append_interaction_to_chat_log
from twilio.rest import Client
import os


app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = '89djhff9lhkd93'

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')


@app.route('/mybot', methods=['POST'])
async def mybot():
    try:
        incoming_msg = request.values['Body']
        chat_log = session.get('chat_log')
        answer = ask(incoming_msg, chat_log)
        session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                            chat_log)
        msg = MessagingResponse()
        msg.message(answer)
        return str(msg)
    except:
        pass
        return "Err"

if __name__ == '__main__':
    app.run(debug=True)