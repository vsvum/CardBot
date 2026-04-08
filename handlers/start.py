
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_start_handler(bot):
    """Регистрирует обработчик команды /start"""
    @bot.message_handler(commands=["start"])
    def cmd_start(message):
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("🔹 Вариант 1", callback_data="opt_1"),
            InlineKeyboardButton("🔹 Вариант 2", callback_data="opt_2"),
            InlineKeyboardButton("🔹 Вариант 3", callback_data="opt_3")
        )
        bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=markup)