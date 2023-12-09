from telebot import custom_filters

from loader import bot
import handlers  # noqa

from utils.default_commands import set_default_commands
# from keyboards import inline, reply
# from states.core import MyStates, storage


if __name__ == "__main__":
    set_default_commands(bot)
    # TODO добавляем фильтр
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()













