from loader import bot

import handlers
from utils.default_commands import set_default_commands
from keyboards import inline, reply
from states.core import MyStates, storage


if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()













