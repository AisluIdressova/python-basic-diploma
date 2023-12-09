from loader import bot
from database.core import crud
from database.models import db, User

from states.core import MyStates


@bot.callback_query_handler(func=lambda call: call.data == 'lookup')
def retrieving_info(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    show_info = crud.retrieve()
    result = show_info(db, User)
    bot.set_state(callback.message.from_user.id, MyStates.looked_up, callback.message.chat.id)
    bot.reply_to(callback.message, result)


if __name__ == '__main__':
    retrieving_info()