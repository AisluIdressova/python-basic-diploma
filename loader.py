import telebot

from config_data.config import SiteSettings


from telebot.storage import StateMemoryStorage


bot_token = SiteSettings()
storage = StateMemoryStorage()

bot = telebot.TeleBot(token=bot_token.token.get_secret_value(), state_storage=storage)