from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard():
    """Создает клавиатуру главного меню"""
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton("📦 Доставка", callback_data="opt_delivery"))
    markup.add(InlineKeyboardButton("💰 Оплата", callback_data="opt_payment"))
    markup.add(InlineKeyboardButton("🆘 Поддержка", callback_data="opt_support"))
    
    return markup

def register_start_handler(bot):
    @bot.message_handler(commands=['start'])
    def cmd_start(message):
        bot.send_message(
            message.chat.id,
            "Привет! 👋 Выберите раздел меню:",
            reply_markup=get_main_menu_keyboard()
        )