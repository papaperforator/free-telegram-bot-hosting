import os

import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup


BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Не задана переменная BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Привет"), KeyboardButton("Помощь"))
    bot.reply_to(message, "Привет! Я работаю. Напишите /help.", reply_markup=keyboard)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.reply_to(message, "Напишите «Привет» или отправьте /start.")


@bot.message_handler(func=lambda message: message.text is not None)
def handle_text(message):
    text = message.text.strip().casefold()
    if text in {"привет", "здравствуйте", "hello"}:
        bot.reply_to(message, "И вам привет!")
    elif text == "помощь":
        handle_help(message)
    else:
        bot.reply_to(message, "Не понял. Отправьте /help.")


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
