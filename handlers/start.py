
from bot import bot
from keyboards.inline import get_three_buttons_keybo

@bot.message_handler(commands=['start'])
def send_start(message):
    markup = get_three_buttons_keyboard()
    bot.send_message(
        message.chat.id, 
        "Привет! Выберите действие:", 
        reply_markup=markup
    )


