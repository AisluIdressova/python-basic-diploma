from telebot import types

from database.models import User, db
from site_API.core import site_api, url, headers, querystring
from database.core import crud
from tg_api.util.core import bot







@bot.callback_query_handler(func=lambda call: call.data == 'search')
def searching_airport(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    bot.reply_to(callback.message, 'Напишите название города')



@bot.callback_query_handler(func=lambda call: call.data == 'lookup')
def retrieving_info(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    show_info = crud.retrieve()
    result = show_info(db, User)
    bot.reply_to(callback.message, result)



if __name__ == '__main__':
    bot.infinity_polling()
