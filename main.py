import telebot
from telebot import types
import webbrowser
import requests
import json
import sqlite3

bot = telebot.TeleBot('6954900384:AAGv6mWREpfR0pI3KNC8WON12t2fSg9okss')
api = 'dict.1.1.20231121T031116Z.8eda48ac1e32dfe3.a1a5dddc8cfff43da92ee5995d6b62e875d38633'
language = ''
result = ''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Привет👋'),
               types.KeyboardButton('Отправить номер телефона', request_contact=True),
               types.KeyboardButton('Отправить геолокацию', request_location=True))
    file = open('privet.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, f'<b><em>Рада вас видеть, {message.from_user.first_name}</em></b>',
                 parse_mode='html')
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    markup2 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Переводить слова', callback_data='translate')
    btn2 = types.InlineKeyboardButton('Мой словарь', callback_data='dictionary')
    markup2.add(btn1,btn2)
    bot.reply_to(message, '...', reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, 'Я - TranslateSample. Мои возможности: ',
                     reply_markup=markup2)

@bot.message_handler(commands=['click'])
def clicker(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Открыть'))
    bot.send_message(message.chat.id, 'Нажмите открыть', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=['site'])
def web_message(message):
    webbrowser.open('https://translate.yandex.com/')
    bot.send_message(message.chat.id, 'Переходим на сайт')


@bot.callback_query_handler(func=lambda call: call.data == 'translate')
def callback_message(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Я - TranslateSample. Мои возможности: ', reply_markup=None)
    markup3 = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('EN-RU')
    btn2 = types.KeyboardButton('RU-EN')
    btn3 = types.KeyboardButton('DE-RU')
    btn4 = types.KeyboardButton('RU-DE')
    btn5 = types.KeyboardButton('FR-RU')
    btn6 = types.KeyboardButton('RU-FR')
    markup3.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.reply_to(callback.message, 'Выберите языки: ', reply_markup=markup3)
    bot.register_next_step_handler(callback.message, checker)
def checker(message):
    if message.text.lower() in ['en-ru', 'ru-en', 'de-ru', 'ru-de', 'fr-ru', 'ru-fr']:
        global language
        language = message.text.lower()
        bot.reply_to(message, 'Вы выбрали языки. Введите слово', reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.reply_to(message, 'Ошибка! Выберите языки')
        bot.register_next_step_handler(message, checker)


@bot.message_handler(func=lambda message: True)
def translator(message):
    try:
        word = message.text
        answer = requests.get(f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={api}&lang={language}&text={word}')
        answer = json.loads(answer.text)
        bot.reply_to(message, f'<b><em>{answer["def"][0]["text"]}\t{answer["def"][0]["tr"][0]["text"]}</em></b>',
                     parse_mode='html')
        bot.reply_to(message, 'Хотите использовать словарь нажмите /click')
    except Exception:
        bot.reply_to(message, 'Неверное слово. Напишите правильное слово заново или начните сначала /click')


@bot.callback_query_handler(func=lambda call: call.data == 'dictionary')
def make_table(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Я - TranslateSample. Мои возможности: ', reply_markup=None)
    with sqlite3.connect('itdictbot.sql') as connection:
        bot_cursor = connection.cursor()
        bot_cursor.execute("CREATE TABLE IF NOT EXISTS dictionary (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                           "word varchar(100), translation varchar(100))")
        connection.commit()
        bot_cursor.close()
    markup5 = types.InlineKeyboardMarkup()
    markup5.add(types.InlineKeyboardButton('Посмотреть словарь', callback_data='view'))
    markup5.row(types.InlineKeyboardButton('Добавить слово', callback_data='add'),
                types.InlineKeyboardButton('Удалить слово', callback_data='remove'))
    bot.reply_to(callback.message, 'Выберите действие', reply_markup=markup5)


@bot.callback_query_handler(func=lambda call: call.data == 'view')
def viewer(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    with sqlite3.connect('itdictbot.sql') as connection:
        bot_cursor = connection.cursor()
        bot_cursor.execute('SELECT * FROM dictionary;')
        sample = bot_cursor.fetchall()
        global result
        result = ''
        for item in sample:
            result += ' | '.join((str(item[0]), item[1], item[2], '\n'))
        markup6 = types.InlineKeyboardMarkup()
        markup6.add(types.InlineKeyboardButton('Посмотреть словарь ', callback_data='view'))
        markup6.row(types.InlineKeyboardButton('Добавить слово ', callback_data='add'),
                    types.InlineKeyboardButton('Удалить слово ', callback_data='remove'))
        if not result:
            bot.reply_to(callback.message, ' Словарь пустой ', reply_markup=markup6)
        else:
            bot.reply_to(callback.message, f'{result}', reply_markup=markup6)
        bot_cursor.close()


@bot.callback_query_handler(func=lambda call: call.data == 'add')
def word_add(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    bot.reply_to(callback.message, 'Напишите слово. Пример: \n<b><em>слово перевод</em></b>', parse_mode='html')
    bot.register_next_step_handler(callback.message, word_input)
def word_input(message):
    with sqlite3.connect('itdictbot.sql') as connection:
        bot_cursor = connection.cursor()
        list_word = message.text.lower().split()
        if len(list_word) == 2:
            bot_cursor.execute('INSERT INTO dictionary (word, translation) VALUES ("%s", "%s");' % (list_word[0], list_word[1]))
            connection.commit()
            bot_cursor.close()
            markup6 = types.InlineKeyboardMarkup()
            markup6.add(types.InlineKeyboardButton('Посмотреть словарь ', callback_data='view'))
            markup6.row(types.InlineKeyboardButton('Добавить слово ', callback_data='add'),
                        types.InlineKeyboardButton('Удалить слово ', callback_data='remove'))
            bot.reply_to(message, 'Слово сохранено.  Хотите использовать переводчик нажмите /click', reply_markup=markup6)
        else:
            bot.reply_to(message, 'Ошибка! Неправильный ввод. Попробуйте заново')
            bot.register_next_step_handler(message, word_input)


@bot.callback_query_handler(func=lambda call: call.data == 'remove')
def word_remove(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    bot.reply_to(callback.message, 'Напишите номер слова, которое хотите удалить')
    bot.register_next_step_handler(callback.message, removing)
def removing(message):

        with sqlite3.connect('itdictbot.sql') as connection:
            bot_cursor = connection.cursor()
            rm_word = message.text
        if rm_word in result:
            bot_cursor.execute(f"DELETE FROM dictionary WHERE id = {rm_word}")
            connection.commit()
            bot_cursor.close()
            markup6 = types.InlineKeyboardMarkup()
            markup6.add(types.InlineKeyboardButton('Посмотреть словарь ', callback_data='view'))
            markup6.row(types.InlineKeyboardButton('Добавить слово ', callback_data='add'),
                        types.InlineKeyboardButton('Удалить слово ', callback_data='remove'))
            bot.reply_to(message, 'Слово успешно удалено. Хотите использовать переводчик нажмите /click', reply_markup=markup6)
        else:
            bot.reply_to(message, 'Ошибка: введите номер заново!')
            bot.register_next_step_handler(message, removing)


if __name__ == '__main__':
    bot.infinity_polling()
