# Leistungskurve-I

## Projektmitglieder:
- Helin Hussein
- Jonathan Hermann

## Projektübersicht
Dieses Projekt umfasst die Erstellung einer Leistungskurve aus den Daten einer CSV-Datei (`Sort_activity.csv`). Das Ziel ist es, die Leistungsdaten zu visualisieren und ein entsprechendes Diagramm im Ordner `figures` zu speichern.

## Systemanforderungen
Das Projekt ist in Python geschrieben und benötigt folgende Pakete:
- pandas
- matplotlib
- numpy

## Setup-Anleitung

### Voraussetzungen
Stellen Sie sicher, dass Python und pip auf Ihrem System installiert sind. 

### Erstellen einer virtuellen Umgebung
Um eine isolierte Umgebung für dieses Projekt zu schaffen, folgen Sie diesen Schritten zur Erstellung einer virtuellen Umgebung:

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
.\.venv\Scripts\activate
```

### Installation der Abhängigkeiten
Installieren Sie die benötigten Pakete über das bereitgestellte Requirements-File:

```bash
pip install -r requirements.txt
```

### Ausführen des Programms
Nach der Installation der Abhängigkeiten können Sie das Programm ausführen, um die Leistungskurve zu erzeugen:

```bash
python main.py
```

## Funktion des Codes
Der Code führt folgende Schritte aus:
1. Einlesen der Daten aus der Datei `Sort_activity.csv`.
2. Überprüfung, ob die notwendige Spalte `PowerOriginal` vorhanden ist.
3. Bereinigung der Daten, Sortierung und Umkehrung der Reihenfolge.
4. Erstellung eines Plots, der die Leistung über die Zeit darstellt.
5. Speichern des Plots im Ordner `figures`.

Für detaillierte Informationen zur Funktionsweise des Codes siehe die Kommentare im Quellcode.
