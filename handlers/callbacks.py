# handlers/callbacks.py

# 🔹 ХРАНИЛИЩЕ ОТВЕТОВ (хранится здесь)
BUTTON_RESPONSES = {
    "opt_1": "📩 Вы выбрали первый вариант!\nТекст для раздела 1.",
    "opt_2": "📩 Вы выбрали второй вариант!\nТекст для раздела 2.",
    "opt_3": "📩 Вы выбрали третий вариант!\nТекст для раздела 3."
}

def register_menu_callbacks(bot):
    """Регистрирует обработчик нажатий на inline-кнопки"""
    @bot.callback_query_handler(func=lambda call: call.data in BUTTON_RESPONSES)
    def handle_menu_click(call):
        bot.answer_callback_query(call.id)  # Убираем "часики"
        try:
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=BUTTON_RESPONSES[call.data]
            )
        except Exception:
            pass  # Игнорируем, если сообщение уже изменено или удалено