from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .start import get_main_menu_keyboard  # Чтобы кнопка "Назад" могла вернуть меню

def register_menu_callbacks(bot):
    # 📝 Тексты, которые покажутся при нажатии кнопок
    MENU_TEXTS = {
        "opt_delivery": "📦 Информация обо мне:\n• Полное имя:Иван Петрович\n• Никнейм:vsvum\n• Роль: Python-разработчик\n• Локация:Санкт-Питербург",
        
        "opt_support": "🆘 Связатся:\nНапишите нам: @error_0100"
    }

    @bot.callback_query_handler(func=lambda call: call.data in MENU_TEXTS)
    def handle_menu_click(call):
        bot.answer_callback_query(call.id)  # ⚡ Убирает "часики" загрузки в Telegram
        
        # Создаем кнопку "Назад"
        back_markup = InlineKeyboardMarkup()
        back_markup.add(InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_menu"))

        # Заменяем сообщение с кнопками на текст + кнопку "Назад"
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=MENU_TEXTS[call.data],
            reply_markup=back_markup
        )

    @bot.callback_query_handler(func=lambda call: call.data == "back_to_menu")
    def handle_back(call):
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Привет! 👋 Выберите раздел меню:",
            reply_markup=get_main_menu_keyboard()
        )