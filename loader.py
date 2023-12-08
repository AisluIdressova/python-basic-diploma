import telebot

from config_data.config import SiteSettings


from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()



bot_token = SiteSettings()

bot = telebot.TeleBot(token=bot_token.token.get_secret_value(), state_storage=storage)