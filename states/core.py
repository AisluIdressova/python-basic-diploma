from telebot.handler_backends import State, StatesGroup

# TODO лишнее закоментировал
# from telebot import custom_filters
# from telebot.storage import StateMemoryStorage
# storage = StateMemoryStorage()


class MyStates(StatesGroup):
    said_hello = State()
    flight_search = State()
    looked_up = State()
