import telebot
token='7108946789:AAHhCzGsliZb4fb5MQilxKM06toxGQpGNgs'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()