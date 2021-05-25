import os
import schedule
import time
import telebot
import krakenex
from pykrakenapi import KrakenAPI

API_KEY = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')

api = API_KEY
chatid = CHAT_ID

bot = telebot.TeleBot(api)
api = krakenex.API()
k = KrakenAPI(api)
coins = ["BTC", "ETH", "DOGE", "ADA", "XRP"]
alerttime = [":00",":05",":10",":15",":20",":25",":30",":35",":40",":45",":50",":55"]

def price(pair):
    val = k.get_ticker_information(pair)
    return "{}: ${}".format(pair, val.a[0][0])

def price_alert():
    text = ""
    for coin in coins:
        pair = coin + "USD"
        text = text + price(pair) + "\n"
    bot.send_message(chatid, text)

for min in alerttime:
    schedule.every().hour.at(min).do(price_alert)

while True:
    schedule.run_pending()
    time.sleep(1)