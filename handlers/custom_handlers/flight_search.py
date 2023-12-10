from states.core import MyStates
from loader import bot
from telebot import types


def make_state_flight_search(message):
    bot.set_state(message.from_user.id, MyStates.flight_search, message.chat.id)
    bot.send_message(message.chat.id, 'Напишите название города', reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    make_state_flight_search()
