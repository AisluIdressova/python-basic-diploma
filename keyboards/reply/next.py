from telebot import types


next_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
next_reply.row(types.KeyboardButton('Продолжить'))
