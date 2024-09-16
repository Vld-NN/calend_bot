from http.client import responses

import telegram
from telegram import BotCommand, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime, timedelta
import requests

def get_holiday():
    url = 'http://holidays.github.io/api/v1/countries/{}/'
    response = requests.get(url.format('ru'))
    holidays = response.json()['data']
    today = datetime.now().strftime('%Y-%m-%d')
    today_holiday = next((h for h in holidays if h['date'] == today), None)
    return today_holiday

