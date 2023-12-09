from loader import bot

from handlers.default_handlers import start, echo, help
from handlers.custom_handlers import callback_lookup, callback_search, on_click, api_request
from utils.default_commands import set_default_commands
from keyboards import inline, reply
from states.core import MyStates, storage


if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()













