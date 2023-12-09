
from loader import bot

from states.core import MyStates

from keyboards.reply.start_reply import markup




@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, f'<b>Добро пожаловать, {message.from_user.first_name}\n'
                          f'Меня зовут - AirportCityFinderBot\n'
                          f'Я умею находить название всех аэропортов\n'
                          f'выбранного города</b>', parse_mode='html', reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.said_hello, message.chat.id)


if __name__=='__main__':
    say_hello()