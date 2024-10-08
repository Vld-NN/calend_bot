from asyncore import dispatcher
from http.client import responses

import telegram
from telegram import BotCommand, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime, timedelta
import requests

def get_holidays():
    url = 'http://holidays.github.io/api/v1/countries/{}/'
    response = requests.get(url.format('ru'))
    holidays = response.json()['data']
    today = datetime.now().strftime('%Y-%m-%d')
    today_holiday = next((h for h in holidays if h['date'] == today), None)
    return today_holiday

def start(update, context):
    update.message.reply_text('Привет! Я календарь праздников! Напиши /today, чтобы узнать какой сегодня праздник.')

def today(update, context):
    holiday = get_holidays()
    if holiday is not None:
        update.message.reply_text(f'Сегодня отмечается {holiday['name']}. Празднуем!')
    else:
        update.message.reply_text('Сегодня нет никаких праздников. Можно просто насладиться днем.')

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(today_handler)

updater.start_polling()
updater.idle()

print('Bot started')
