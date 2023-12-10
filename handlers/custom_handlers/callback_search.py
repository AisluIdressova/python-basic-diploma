from loader import bot
from handlers.custom_handlers.flight_search import make_state_flight_search
from keyboards import next_reply


@bot.callback_query_handler(func=lambda call: call.data == 'search')
def searching_airport(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Пример запроса\nГород: Москва', reply_markup=None)
    bot.send_message(callback.message.chat.id, 'Шеремьетево', reply_markup=next_reply)
    bot.register_next_step_handler(callback.message, make_state_flight_search)


if __name__ == '__main__':
    searching_airport()