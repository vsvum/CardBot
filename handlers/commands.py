from bot import bot

# Путь к фото (локальный или URL)
FIRST_PHOTO = "photos/(вставить фото).jpg"  # или https://...
FIRST_TEXT = """
👋 <b>Привет! Это небольшая Визитка про меня.</b>

<b>Анкета:<b>

🔹 Полное имя: [Айдар Валиуллин]
🔹 Никнейм / Как обращаться: [@vsvum]
🔹 Должность / Роль: [Python-разработчик / Студент / Фрилансер]
🔹 Локация: [Санкт-Питербург, Россия / Удалённо]
🔹 Часовой пояс: [UTC+2]
🔹 Языки: [Русский (родной)]

"""





@bot.message_handler(commands=["start"])
def send_first_step(message):
    # Отправляем фото + текст + кнопку
    with open(FIRST_PHOTO, "rb") as photo:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=FIRST_TEXT,
            reply_markup=get_continue_keyboard("step_2")
        )