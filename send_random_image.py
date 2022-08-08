import requests
from telegram import Bot

bot = Bot(token='5435072837:AAEKUbblpnmckxS8ZUaF_-YoPIxPbVOvocI')

URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
# chat_id = 188641435
# text = 'Вам телеграмма!'
# # Отправка сообщения
# bot.send_message(chat_id, text)
# # Отправка изображения
# bot.send_photo(chat_id, URL)

print(response)
# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(type(response[0])) 