import platform
import subprocess
import telebot

BOT_TOKEN = ''
YOUR_CHAT_ID = ''  

bot = telebot.TeleBot(BOT_TOKEN)

def is_computer_on():
    system = platform.system().lower()
    if system == "windows":
        try:
            subprocess.check_output("ping google.com", shell=True)
            return True
        except subprocess.CalledProcessError:
            return False

def send_computer_status():
    if is_computer_on():
        bot.send_message(YOUR_CHAT_ID, "Компьютер включен")
    else:
        bot.send_message(YOUR_CHAT_ID, "Компьютер выключен")

send_computer_status()
