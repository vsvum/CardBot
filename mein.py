import config
from bot import bot
from handlers import start, callbacks  # Импорт регистрирует хендлеры

if __name__ == "__main__":
    print("🟢 Бот запущен...")
    bot.infinity_polling()