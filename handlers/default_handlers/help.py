
from loader import bot


@bot.message_handler(state='*', commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, "Действие отменено")
    bot.delete_state(message.from_user.id, message.chat.id)

if __name__ == '__main__':
    bot_help()