from loader import bot

from handlers import say_hello, on_click
from utils.default_commands import set_default_commands
from keyboards import inline, reply
from states.core import MyStates, storage


if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()













