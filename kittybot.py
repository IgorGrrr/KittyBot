import os

from dotenv import load_dotenv

import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

#bot = Bot(token='5435072837:AAEKUbblpnmckxS8ZUaF_-YoPIxPbVOvocI')

#chat_id = 188641435
# text = 'Вам письмо бом бом'
# bot.send_message(chat_id, text)
load_dotenv()

secret_token = os.getenv('TOKEN')

updater = Updater(token=secret_token)
URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return(random_cat)

def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id,
                             text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
                             reply_markup=button
                             )
    context.bot.send_photo(chat.id, get_new_image())

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

updater.start_polling()

updater.idle()