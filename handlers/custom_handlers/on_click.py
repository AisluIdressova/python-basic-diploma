from telebot import types

from loader import bot

from states.core import MyStates


from keyboards.inline.inline_keyb import inline_markup




@bot.message_handler(state=MyStates.said_hello)
def on_click(message):
    bot.reply_to(message, 'Мои возможности', reply_markup=types.ReplyKeyboardRemove())
    bot.reply_to(message, 'Выберите действие', reply_markup=inline_markup)
