from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
import re

import requests
import alerts
import json
app = Flask(__name__)




sslify = SSLify(app)
token = '7875995471:AAFYcnSDTwKB-A7OffWoSeMquN6Y-1i32fc'
URL = "https://api.telegram.org/bot" + token + '/'

global last_update_id
#https://api.telegram.org/bot7875995471:AAFYcnSDTwKB-A7OffWoSeMquN6Y-1i32fc\setWebhook?url=https://80bb-141-138-108-110.ngrok-free.app/
last_update_id = 0

def write_json(data, filename = 'answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 2, ensure_ascii=False)


def get_updates():

    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def send_message(chat_id, text = 'Unknown command'):
    url = URL + 'sendmessage'
    answer = {'chat_id' : chat_id, 'text':text, 'offset': last_update_id}
    r = requests.post(url, json=answer)

    return r.json()

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        pattern = r'/\w+'
        if(re.search(pattern, message) and message is not None and len(message) > 4):
            if(re.search(pattern, message).group()[1:] == 'start'):
                send_message(chat_id, text = 'Слеш (/) та назва області, що цікавить.')
            else:
                alertResult = alerts.get_data(alerts.parse_text(message))
                send_message(chat_id, text = alertResult)
        else:
            send_message(chat_id, text = 'Type correct (Вінницька область)')
        #write_json(r)
        return jsonify(r)
    return '<h1>Alert bot</h1>'


if __name__ == '__main__':
    app.run()
