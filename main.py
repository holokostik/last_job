import telebot
import datetime
import time
import schedule

bot = telebot.TeleBot('dfsfd')

# Создание клавиатуры с кнопкой 'Создать напоминание'
markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(telebot.types.KeyboardButton('Создать напоминание'))
markup.add(telebot.types.KeyboardButton('Создать ежедневное напоминание'))


@bot.message_handler(commands=['start'])
def start(message):
    # Добавление клавиатуры с кнопкой 'Создать напоминание'
    bot.send_message(message.chat.id, 'Привет! Я - бот, который может помогать тебе соблюдать распорядок дня'
                                      'и выполнять намеченные планы. Я умею присылать напоминания о твоих делах,'
                                      'если ты попросишь <3 Нажми кнопку "Создать напоминание",'
                                      ' чтобы создать новое напоминание.', reply_markup=markup)


# вот сюда все текстовые ответы на проверку придут
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Создать напоминание':
        bot.send_message(
            chat_id=message.chat.id,
            text="Введите дату и время и текст напоминания в формате: ЧЧ:ММ ДД-ММ-ГГГГ Напоминание",
        )
        bot.register_next_step_handler(message, handle_reminder)



