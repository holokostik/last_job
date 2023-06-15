import telebot
import emoji

bot = telebot.TeleBot('6296708608:AAGW_e4ZSfdIjqNjc09zVW2T8cPUOW4ZVKA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я - бот, который может помогать тебе соблюдать распорядок дня'
                                      'и выполнять намеченные планы. Я умею присылать напоминания о твоих делах,'
                                      'если ты попросишь <3')


bot.polling(none_stop=True)
