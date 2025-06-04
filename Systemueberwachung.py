import psutil
import platform
import time
from datetime import datetime, timedelta

def get_system_info():
    system_name = platform.node()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    uptime = timedelta(seconds=int(time.time() - psutil.boot_time()))
    jetzt = datetime.now()

    print("📊 Systemüberwachung")
    print("==========================")
    print(f"🕒 Aktuelle Zeit      : {jetzt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🖥  Geräte-Name       : {system_name}")
    print(f"🧠 CPU-Auslastung     : {cpu_usage}%")
    print(f"💾 RAM-Auslastung     : {memory_usage}%")
    print(f"⏱️  Laufzeit des Systems: {uptime}")
    print("==========================\n")

while True:
    get_system_info()
    time.sleep(3)

