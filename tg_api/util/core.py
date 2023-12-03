import telebot

from setting import SiteSettings


bot_token = SiteSettings()

bot = telebot.TeleBot(bot_token.token.get_secret_value())
