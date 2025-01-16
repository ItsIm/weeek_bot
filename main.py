import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from environs import Env

# Инициализация окружения
env = Env()
env.read_env()

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Получаем токены и ID из переменных окружения
TELEGRAM_BOT_TOKEN = env("TELEGRAM_BOT_TOKEN")
AUTH_HEADER = {'Authorization': env("WEEK_AUTH_TOKEN")}
ALLOWED_USER_ID = env.int("ALLOWED_USER_ID")  # Преобразуем в int
WEEK_USER_ID = env.str("ALLOWED_USER_ID")
API_URl = env.str("API_URl")
PROJECT_ID = env.int("PROJECT_ID")

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Отправь мне сообщение, и я создам задачу.')


@dp.message_handler(lambda message: message.from_user.id != ALLOWED_USER_ID)
async def restricted_access(message: types.Message):
    return


@dp.message_handler(lambda message: message.from_user.id == ALLOWED_USER_ID)
async def handle_message(message: types.Message):
    user_message = message.text

    # Формируем данные для POST-запроса
    data = {
        "title": user_message,
        "type": "action",
        "projectId": PROJECT_ID,
        "customFields": {}
    }

    try:
        # Отправляем POST-запрос
        response = requests.post(f'{API_URl}/tm/tasks', headers=AUTH_HEADER, json=data)
        response.raise_for_status()

        # Уведомляем пользователя об успешном выполнении
        await message.reply('Запрос успешно отправлен!')
    except requests.exceptions.RequestException as e:
        logging.error(f'Ошибка при отправке запроса: {e}')
        await message.reply('Произошла ошибка при отправке запроса.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
