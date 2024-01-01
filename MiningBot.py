import telebot
import pynvml

pynvml.nvmlInit()
device_count = pynvml.nvmlDeviceGetCount()

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")

for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        gpu_utilization = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        gpu_temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        print(f"Видеокарта {i+1}: {gpu_name}")
        print(f"Загрузка видеокарты: {gpu_utilization}%")
        print(f"Температура видеокарты: {gpu_temperature}°C")

information = ("Видеокарта "+ gpu_name + "\n" 
               + "Загрузка видеокарты: " + str(gpu_utilization) + "%" + "\n" 
               + "Температура видеокарты: " + str(gpu_temperature) + "%" )

@bot.message_handler(commands=['info'])
def answer(message):
    bot.send_message(message.chat.id, information)
    return answer

bot.polling(none_stop=True)
