import os
import schedule
import time
import telebot
from pycoingecko import CoinGeckoAPI


#Telegram setup
TELEBOT_API_KEY = os.getenv('TELEBOT_API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
telebotapi = TELEBOT_API_KEY
chatid = CHAT_ID
bot = telebot.TeleBot(telebotapi)

def price_alert():
    bot.send_message(chatid, price())

#CoinGecko setup
cg = CoinGeckoAPI()

portfolio = {
    'ethereum':'ETH',
    'bitcoin':'BTC',
    'dogecoin':'DOGE',
    'cardano':'ADA',
    'pancakeswap-token':'CAKE',
    'ravencoin':'RVN',
    'ripple':'XRP',
    'solana':'SOL',
    'apeswap-finance':'BANANA'
}

crypto_list =  list(portfolio.keys())

def price():
    values = cg.get_price(ids=crypto_list, vs_currencies='usd')
    text = ''

    for crypto,value in values.items():
        for prop,val in value.items():
            text = text + portfolio[crypto] + ": $" + val + "\n"

    return text


#Scheduling
alerttime = [":00",":05",":10",":15",":20",":25",":30",":35",":40",":45",":50",":55"]

for min in alerttime:
    schedule.every().hour.at(min).do(price_alert)

while True:
    schedule.run_pending()
    time.sleep(1)
