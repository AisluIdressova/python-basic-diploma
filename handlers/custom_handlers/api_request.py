from states.core import MyStates

from loader import bot

from utils.core import site_api, url, headers, querystring
from loader import bot
from database.models import User, db
from datetime import datetime
from database.core import crud


@bot.message_handler(state=MyStates.flight_search)
def make_request(message):
    if message.text in ['Нет', 'нет', 'НЕТ']:
        bot.reply_to(message, 'Хорошо. Продолжайте вводить города')
    elif message.text in ['Да', 'да', 'ДА']:
        bot.set_state(message.from_user.id, MyStates.said_hello, message.chat.id)
    else:
        check_api = site_api.get_info()
        result = check_api(url, headers, querystring, message.text)
        if not result:
            bot.reply_to(message, 'Ошибка! Попробуйте заново.')
        else:
            bot.reply_to(message, result)
            bot.send_message(message.chat.id, 'Напишите следующий город\nВернуться на главное меню: (да/нет)')

        current_time = datetime.now().strftime("%H-%M-%S  %d/%m/%Y")
        data = [{'message': message.text, 'date': current_time}]

        db_write = crud.create()
        db_write(db, User, *data)

if __name__ == '__main__':
    make_request()