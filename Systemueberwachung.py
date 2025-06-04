# Systemüberwachungstool entwickelt von Faisal Al-Muraqab
# Dieses einfache Python-Skript zeigt die aktuelle CPU-, RAM-Auslastung und Systemlaufzeit an.

import psutil
import platform
import time
from datetime import timedelta

def get_system_info():
    system_name = platform.node()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    uptime = timedelta(seconds=int(time.time() - psutil.boot_time()))

    print("📊 Systemüberwachung")
    print("==========================")
    print(f"🖥  Geräte-Name       : {system_name}")
    print(f"🧠 CPU-Auslastung     : {cpu_usage}%")
    print(f"💾 RAM-Auslastung     : {memory_usage}%")
    print(f"⏱️  Laufzeit des Systems: {uptime}")
    print("==========================\n")

while True:
    get_system_info()
    time.sleep(3)