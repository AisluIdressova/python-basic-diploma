from telebot import types

from loader import bot

from states.core import MyStates

from keyboards.inline.inline_keyb import inline_markup


@bot.message_handler(state=MyStates.said_hello)
def on_click(message):
    bot.reply_to(message, 'Мои возможности', reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=inline_markup)
    print(bot.get_state(message.from_user.id, message.chat.id), message.chat)


if __name__ == '__main__':
    on_click()
