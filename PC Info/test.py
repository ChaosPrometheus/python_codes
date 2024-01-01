import psutil
import pynvml

pynvml.nvmlInit()
device_count = pynvml.nvmlDeviceGetCount()

memory_info = psutil.virtual_memory()
print("\nИнформация о памяти:")
print(f"Всего памяти: {memory_info.total / (1024 ** 3):.2f} GB")
print(f"Доступно памяти: {memory_info.available / (1024 ** 3):.2f} GB")

disk_info = psutil.disk_partitions()
print("\nИнформация о дисках:")
for partition in disk_info:
    print(f"Устройство: {partition.device}")
    print(f"Монтируемая точка: {partition.mountpoint}")

network_info = psutil.net_if_addrs()
print("\nИнформация о сетевых интерфейсах:")
for interface, addresses in network_info.items():
    print(f"Интерфейс: {interface}")
    for address in addresses:
        print(f"Тип адреса: {address.family}")
        print(f"Адрес: {address.address}")

battery_info = psutil.sensors_battery()
if battery_info:
    print("\nИнформация о батарее:")
    print(f"Заряд батареи: {battery_info.percent}%")
    print(f"Статус батареи: {battery_info.power_plugged}")
else:
    print("\nИнформация о батарее недоступна.")

cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
print("\nИнформация о загрузке CPU:")
for core, usage in enumerate(cpu_percent):
    print(f"Ядро {core + 1}: {usage}%")

for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        gpu_utilization = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        gpu_temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        print(f"Видеокарта {i+1}: {gpu_name}")
        print(f"Загрузка видеокарты: {gpu_utilization}%")
        print(f"Температура видеокарты: {gpu_temperature}°C")

pynvml.nvmlShutdown()