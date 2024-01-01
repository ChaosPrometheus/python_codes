import os
import googleapiclient.discovery
import time
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Command

telegram_token = '5579059495:AAG6trIVGPK_3Ev64cVfAzyZH0TQBFtjeLI'# токен телеграм бота

chat_id = '@mechgroupoff'# айди канала

api_key = 'AIzaSyDlRDZqMujkh7p9N3NUhDn1rFbYwqOw3NA'# надо создать апи токен из ютуб консоль

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

channel_id = 'UCp1s7sfnbGns_X4neE1kiQQ'# адрес канала

# Инициализация бота и диспетчера
bot = Bot(token=telegram_token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Множество для хранения ссылок на видео
video_urls = set()

# Функция для получения списка ссылок на видео в канале
def get_video_urls():
    response = youtube.search().list(
        channelId=channel_id,
        order='date',
        part='id',
        maxResults=10
    ).execute()

    video_urls = set()
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_urls.add(video_url)

    return video_urls

# Проверка наличия новых видео и отправка уведомления, если есть новые видео
async def check_for_new_videos():
    global video_urls
    new_video_urls = get_video_urls() - video_urls
    if new_video_urls:
        video_urls.update(new_video_urls)
        for video_url in new_video_urls:
            await send_telegram_message(f"Найдено новое видео: {video_url}")

# Функция для отправки сообщения через Telegram бота
async def send_telegram_message(message):
    await bot.send_message(chat_id, message)

# Обработчик команды /start
@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.reply("Привет! Я буду отправлять уведомления о новых видео на вашем YouTube канале.")

# Бесконечный цикл проверки каждые 5 минут
async def schedule_check():
    while True:
        await check_for_new_videos()
        await asyncio.sleep(300)  # Пауза в 5 минут (300 секунд)

# Запуск бота
async def main():
    await bot.send_message(chat_id, "Бот запущен.")
    await schedule_check()

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

# Конец кода
