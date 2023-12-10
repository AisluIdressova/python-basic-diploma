from loader import bot
from handlers.custom_handlers.flight_search import make_state_flight_search

@bot.callback_query_handler(func=lambda call: call.data == 'search')
def searching_airport(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выбор сделан', reply_markup=None)
    bot.reply_to(callback.message, 'Напишите название города')
    bot.register_next_step_handler(callback.message, make_state_flight_search)


if __name__ == '__main__':
    searching_airport()