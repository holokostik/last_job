import telebot

bot = telebot.TeleBot('6296708608:AAGW_e4ZSfdIjqNjc09zVW2T8cPUOW4ZVKA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


bot.polling(none_stop=True)
