from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Токен вашего бота
BOT_TOKEN = '7990023498:AAEm1HdPCXobsKHyUuQFi-rV_wOFr24KEFQ'
# URL вашего веб-приложения
WEB_APP_URL = 'https://test002-weld.vercel.app'

# Обработчик для главной страницы
@app.route('/')
def index():
    return "Добро пожаловать в Telegram Mini App!"

# Обработчик для вебхука Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    # Если пользователь отправил команду /start
    if text == '/start':
        # Отправляем сообщение с кнопкой для открытия Mini App
        send_message(chat_id, "Нажмите кнопку ниже, чтобы открыть Mini App!", WEB_APP_URL)

    return jsonify({'status': 'ok'})

# Функция для отправки сообщения через Telegram Bot API
def send_message(chat_id, text, web_app_url):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            'inline_keyboard': [
                [{
                    'text': 'Открыть Mini App',
                    'web_app': {'url': web_app_url}
                }]
            ]
        }
    }
    response = requests.post(url, json=payload)
    return response.json()

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)