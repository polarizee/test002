from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = '7990023498:AAEm1HdPCXobsKHyUuQFi-rV_wOFr24KEFQ'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    if text == '/start':
        send_message(chat_id, "Привет! Это ваш бот.")

    return jsonify({'status': 'ok'})

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)