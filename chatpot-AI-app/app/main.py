from flask import Flask, request, jsonify, session
from twilio.twiml.messaging_response import MessagingResponse
from app.chatpot import append_interaction_to_chat_log, ask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my secret'

@app.route('/bot', methods=['POST'])
def bot():
    
    incoming_msg = request.values['Body']
    print(incoming_msg)
    chat_log = session.get('chat_log')

    answer = ask(question=incoming_msg, chat_log=chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)

    r = MessagingResponse()
    r.message(answer)
    print(str(r))
    return str(r)