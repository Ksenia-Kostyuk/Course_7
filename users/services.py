import requests
from config import settings


def reminder_of_a_habit(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id
    }
    response = requests.get(f'{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage', params=params)
