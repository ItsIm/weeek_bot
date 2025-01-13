# Telegram Bot

Этот проект представляет собой Telegram-бота, который принимает сообщения от определенного пользователя и отправляет их на указанный API. Бот использует библиотеку `aiogram` для работы с Telegram API и `requests` для отправки HTTP-запросов.

## Функциональность

- Бот принимает текстовые сообщения только от пользователя с определённым ID.
- При получении сообщения бот отправляет его на указанный API с заданными параметрами.
- Пользователь получает уведомление об успешной отправке запроса или об ошибке, если она произошла.

## Установка

### 1. Клонирование репозитория

Сначала клонируйте репозиторий на ваш локальный компьютер:

```bash
git clone https://github.com/ItsIm/weeek_bot.git
cd weeek_bot
```

### 2. Установка зависимостей

Убедитесь, что у вас установлен Python 3.7 или выше. Затем установите необходимые зависимости с помощью pip:

```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

```bash
cp .env.dist .env
```

## Запуск

После настройки переменных окружения запустите бота с помощью следующей команды:

```bash
python main.py
```

## Использование

После запуска бота откройте Telegram и найдите своего бота по имени.
Отправьте команду /start, чтобы получить приветственное сообщение.
Отправьте любое текстовое сообщение. Бот проверит ваш ID и, если вы являетесь разрешенным пользователем, создаст задачу.
Вы получите уведомление об успешной отправке запроса или об ошибке, если она произошла.