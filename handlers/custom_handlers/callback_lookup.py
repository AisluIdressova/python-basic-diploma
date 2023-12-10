from loader import bot

from database.core import crud
from database.models import db, User



@bot.callback_query_handler(func=lambda call: call.data == 'lookup')
def reply_to_search(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выбор сделан', reply_markup=None)
    show_info = crud.retrieve()
    result = show_info(db, User)
    bot.reply_to(callback.message, result)




if __name__ == '__main__':
    reply_to_search()