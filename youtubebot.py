import os
import googleapiclient.discovery
import googleapiclient.errors
import time

api_key = ''
channel_id = ''

def get_latest_video_id(api_key, channel_id):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(part='id', channelId=channel_id, maxResults=1, order='date')
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return video_id

def check_for_new_video(api_key, channel_id):
    latest_video_id = get_latest_video_id(api_key, channel_id)
    if not os.path.isfile('latest_video_id.txt'):
        with open('latest_video_id.txt', 'w') as file:
            file.write(latest_video_id)
            return False
    with open('latest_video_id.txt', 'r') as file:
        stored_video_id = file.read()
        if latest_video_id != stored_video_id:
            with open('latest_video_id.txt', 'w') as file:
                file.write(latest_video_id)
            return True
    return False

while True:
    if check_for_new_video(api_key, channel_id):
        latest_video_id = get_latest_video_id(api_key, channel_id)
        video_url = f'https://www.youtube.com/watch?v={latest_video_id}'
        print(f'Новое видео: {video_url}')
        # Здесь вы можете вставить код для отправки ссылки куда-либо (например, через email или мессенджер)
    time.sleep(15)  # Проверка каждую минуту
