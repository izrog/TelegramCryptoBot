import os
import schedule
import time
import telebot
import krakenex
from pykrakenapi import KrakenAPI

TELEBOT_API_KEY = os.getenv('TELEBOT_API_KEY')
CHAT_ID = os.getenv('CHAT_ID')

telebotapi = TELEBOT_API_KEY
chatid = CHAT_ID

bot = telebot.TeleBot(telebotapi)
api = krakenex.API()
k = KrakenAPI(api)
coins = ['ADA','DOGE','ETH','BTC','XRP']
pairs = "ADAUSD,XDGUSD,XETHZUSD,XXBTZUSD,XXRPZUSD"
alerttime = [":00",":05",":10",":15",":20",":28",":30",":35",":40",":45",":50",":55"]

def price(pair):
    val = k.get_ticker_information(pair)
    i  = 0
    text = ""
    for index, coin in val.iterrows():
        text = text + coins[i] + ":$" + coin[0][0] + "\n"
        i += 1
    return text

def price_alert():
    bot.send_message(chatid, price(pairs))

for min in alerttime:
    schedule.every().hour.at(min).do(price_alert)

while True:
    schedule.run_pending()
    time.sleep(1)