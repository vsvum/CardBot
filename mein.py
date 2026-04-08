import telebot
from handlers import register_start_handler, register_menu_callbacks

bot = telebot.TeleBot("8247222389:AAGnNEyuC0ob1KqZ7Xh0Hm5zMgTjEuTkCLU")

# 🔌 Регистрируем обработчик команды /start
register_start_handler(bot)
register_menu_callbacks(bot)

print("✅ Бот запущен")
bot.polling(none_stop=True)