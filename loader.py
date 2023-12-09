import telebot

from config_data.config import SiteSettings

from states.core import storage

from config_data import config





bot_token = SiteSettings()

bot = telebot.TeleBot(token=bot_token.token.get_secret_value(), state_storage=storage)