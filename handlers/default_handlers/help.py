
from loader import bot

from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot



@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    # bot.send_message(message.chat.id, "Действие отменено")
    # bot.delete_state(message.from_user.id, message.chat.id)
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))


if __name__ == '__main__':
    bot_help()