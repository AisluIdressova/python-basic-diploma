from loader import bot

from states.core import MyStates

@bot.callback_query_handler(func=lambda call: call.data == 'search')
def searching_airport(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    bot.set_state(callback.message.from_user.id, MyStates.flight_search, callback.message.chat.id)
    bot.reply_to(callback.message, 'Напишите название города')


if __name__ == '__main__':
    searching_airport()