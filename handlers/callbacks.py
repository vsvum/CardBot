# handlers/callbacks.py
from .start import register_start_handler   # ваш обработчик /start

# 🔹 ХРАНИЛИЩЕ ОТВЕТОВ (хранится прямо в этом файле)
BUTTON_RESPONSES = {
    "opt_1": "📦 Раздел 1: Информация о доставке\n• Курьером: 1-2 дня\n• Самовывоз: бесплатно",
    "opt_2": "💰 Раздел 2: Тарифы и оплата\n• Карта, СБП, наличные",
    "opt_3": "🆘 Раздел 3: Техподдержка\n• Напишите нам: @admin_support"
}

def register_menu_callbacks(bot):
    """Регистрирует обработчик нажатий на inline-кнопки"""

    @bot.callback_query_handler(func=lambda call: call.data in BUTTON_RESPONSES)
    def handle_menu_click(call):
        # 1. Обязательно отвечаем на callback, иначе Telegram покажет "часики"
        bot.answer_callback_query(call.id)

        try:
            # 2. Заменяем сообщение с кнопками на текст из словаря
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=BUTTON_RESPONSES[call.data]
            )
        except Exception:
            # Игнорируем ошибку, если текст уже совпадает или сообщение удалено
            pass