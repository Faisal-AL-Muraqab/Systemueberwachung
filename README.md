# Systemüberwachungstool mit Python 🖥️

## 📌 Projektbeschreibung

Dieses Projekt wurde von Faisal Al-Muraqab entwickelt.  
Es handelt sich um ein einfaches Systemüberwachungstool, das mithilfe der Python-Bibliothek psutil Informationen über die aktuelle CPU- und RAM-Auslastung sowie die Systemlaufzeit anzeigt.

---

## 🧠 Verwendete Technologien

- Python 3.13  
- psutil  
- Standardbibliotheken: platform, time, datetime, csv  
- tkinter (für grafische Benutzeroberfläche)  

---

## 🔍 Funktionsweise

Das Skript zeigt im Abstand von 1 Sekunde folgende Systeminformationen an:

- Geräte-Name  
- CPU-Auslastung in Prozent  
- RAM-Auslastung in Prozent  
- Systemlaufzeit seit dem letzten Start  
- Aktuelles Datum und Uhrzeit  

Die Daten werden sowohl in der Konsole als auch grafisch über eine Tkinter-GUI angezeigt. Zusätzlich werden alle Messwerte automatisch in einer CSV-Datei (`system_data.csv`) gespeichert, um eine spätere Analyse oder Visualisierung zu ermöglichen.

---

## 🆕 Neue Funktionen & Verbesserungen

✅ Aktualisierung der Systeminformationen alle 1 Sekunde  
✅ Integration einer grafischen Benutzeroberfläche (GUI) mit Tkinter  
✅ Automatische Speicherung der Systemdaten in der Datei system_data.csv  
✅ Verbesserte Darstellung der Daten (klare Labels, Icons)  
✅ Strukturierte Datenerfassung für spätere Auswertung  

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

