from states.core import MyStates
from loader import bot

def make_state_flight_search(message):
    bot.set_state(message.from_user.id, MyStates.flight_search, message.chat.id)
    print('asking_city', bot.get_state(message.from_user.id, message.chat.id))


if __name__ == '__main__':
    make_state_flight_search()
