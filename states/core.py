from telebot.handler_backends import State, StatesGroup




class MyStates(StatesGroup):
    said_hello = State()
    flight_search = State()

