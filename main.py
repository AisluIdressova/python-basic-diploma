from telebot import custom_filters

from loader import bot
import handlers  # noqa

from utils.default_commands import set_default_commands



if __name__ == "__main__":
    set_default_commands(bot)
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()













