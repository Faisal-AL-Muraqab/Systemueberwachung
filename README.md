# Systemüberwachungstool mit Python 🖥️

## 📌 Projektbeschreibung

Dieses Projekt wurde von Faisal Al-Muraqab entwickelt.  
Es handelt sich um ein einfaches Systemüberwachungstool, das mithilfe der Python-Bibliothek psutil Informationen über die aktuelle CPU- und RAM-Auslastung sowie die Systemlaufzeit anzeigt.

---

## 🧠 Verwendete Technologien

- Python 3.13
- psutil
- Standardbibliotheken (`platform`, time, `datetime`)

---

## 🔍 Funktionsweise

Das Skript zeigt im Abstand von 3 Sekunden folgende Informationen an:

- Geräte-Name
- CPU-Auslastung in Prozent
- RAM-Auslastung in Prozent
- Systemlaufzeit seit dem letzten Start
- Aktuelles Datum und Uhrzeit

Diese Informationen werden nicht nur in der Konsole angezeigt, sondern auch automatisch in einer CSV-Datei gespeichert. 

---

## 🆕 Neue Funktionen

✅ Speicherung der Systemdaten in der Datei system_data.csv  
✅ Automatische Aktualisierung der Datei alle 3 Sekunden  
✅ Strukturierte Daten für spätere Analyse oder Visualisierung

---

## 📦 Installation & Nutzung

1. Stelle sicher, dass Python 3 installiert ist  
2. Installiere psutil über das Terminal :

   ```bash
   pip install psutil
   ```

3. Speichere das Skript Systemueberwachung.py in einem Ordner deiner Wahl  
4. Öffne das Terminal in diesem Ordner und führe aus: 

   ```bash
   py Systemueberwachung.py  
   ```

