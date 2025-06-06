import psutil
import platform
import time
from datetime import datetime, timedelta
import csv
import os

def get_system_info():
    system_name = platform.node()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    uptime = timedelta(seconds=int(time.time() - psutil.boot_time()))
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return [current_time, system_name, cpu_usage, memory, str(uptime)]

def write_to_csv(data):
    file_exists = os.path.isfile("system_data.csv")

    with open("system_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Zeit", "Geräte-Name", "CPU-Auslastung (%)", "RAM-Auslastung (%)", "Systemlaufzeit"])
        writer.writerow(data)

def display_info(data):
    print("\n📊 Systemüberwachung")
    print("==========================")
    print(f"🕒 Zeit               : {data[0]}")
    print(f"🖥️  Geräte-Name        : {data[1]}")
    print(f"🧠 CPU-Auslastung      : {data[2]}%")
    print(f"💾 RAM-Auslastung      : {data[3]}%")
    print(f"⏱️  Laufzeit des Systems: {data[4]}")
    print("==========================")

while True:
    info = get_system_info()
    display_info(info)
    write_to_csv(info)
    time.sleep(3)