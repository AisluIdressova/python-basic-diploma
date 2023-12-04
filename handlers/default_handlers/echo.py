from site_API.core import site_api, url, headers, querystring
from tg_api.util.core import bot
from database.models import User, db
import datetime
from database.core import crud



@bot.message_handler(func=lambda message: True)
def checker(message):
    check_api = site_api.get_info()
    result = check_api(url, headers, querystring, message.text)
    if not result:
        bot.reply_to(message,'Ошибка! Попробуйте заново.')
    else:
        bot.reply_to(message, result)
        bot.send_message(message.chat.id, 'Напишите следующий город или начните сначала /start')
    db_write = crud.create()
    now = datetime.datetime.now()
    current_time = now.strftime("%H-%M-%S  %d/%m/%Y")
    data = [{'message': message.text, 'date': current_time}]
    db_write(db, User, *data)
