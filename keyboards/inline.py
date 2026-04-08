
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_three_buttons_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🔹 Моя Анкета", callback_data="opt_1"),
        InlineKeyboardButton("🔹 Контакты", callback_data="opt_2"),
        InlineKeyboardButton("🔹 Задать вопрос", callback_data="opt_3")
    )
    return markup