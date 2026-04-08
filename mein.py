import telebot
from handlers import register_start_handler, register_menu_callbacks

bot = telebot.TeleBot("ВАШ_ТОКЕН")

# 🔌 Регистрируем все обработчики, передавая экземпляр бота
register_start_handler(bot)
register_menu_callbacks(bot)

print("✅ Бот запущен")
bot.polling(none_stop=True)