from loader import bot

from database.core import crud
from database.models import db, User

from keyboards import next_reply


@bot.callback_query_handler(func=lambda call: call.data == 'lookup')
def reply_to_search(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выбор сделан', reply_markup=None)
    show_info = crud.retrieve()
    result = show_info(db, User)
    bot.send_message(callback.message.chat.id, result, reply_markup=next_reply)




if __name__ == '__main__':
    reply_to_search()