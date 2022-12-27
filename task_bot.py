import cfg 
import telebot
import requests
bot = telebot.TeleBot(cfg.TOKEN)

res = requests.get(cfg.url).json()
nameusd =(res['Valute']["USD"]['Name'] + ' - ')
valueusd = (res['Valute']["USD"]['Value'])

nameeur =(res['Valute']["EUR"]['Name'] + ' - ')
valueeur = (res['Valute']["EUR"]['Value'])

namecny =(res['Valute']["CNY"]['Name'] + ' - ')
valuecny = (res['Valute']["CNY"]['Value'])



@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Доступные команды:\n /currency_USD\n /currency_EUR\n /currency_CNY")

@bot.message_handler(commands=['currency_USD'])
def send_welcome(message):
	bot.send_message(message.chat.id, nameusd + str(valueusd))

@bot.message_handler(commands=['currency_EUR'])
def send_welcome(message):
	bot.send_message(message.chat.id, nameeur + str(valueeur))

@bot.message_handler(commands=['currency_CNY'])
def send_welcome(message):
	bot.send_message(message.chat.id, namecny + str(valuecny))



bot.infinity_polling()





