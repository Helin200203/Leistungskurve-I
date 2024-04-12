import pandas as pd
import matplotlib.pyplot as plt
import os

from sort import bubble_sort
from load_data import load_data

def plot_data(sorted_power):
    """Erstellt eine Grafik der sortierten Leistungsdaten."""
    plt.figure()
    # Umrechnung der Zeit von Sekunden zu Minuten
    time_in_minutes = [i / 60 for i in range(len(sorted_power))]
    plt.plot(time_in_minutes, sorted_power, label='PowerOriginal')
    plt.title('Leistungskurve über die Zeit')
    plt.xlabel('Zeit (Minuten)')
    plt.ylabel('Leistung (Watt)')
    plt.legend()
    plt.savefig('figures/power_curve.png')
    plt.show()

def check_and_create_directory(directory_name='figures'):
    """Prüft, ob ein Verzeichnis existiert, und erstellt es bei Bedarf."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def main():
    # Daten aus einer CSV-Datei laden
    data = load_data('Sort_activity.csv')
    print(data)

    # Stelle sicher, dass die benötigte Spalte vorhanden ist
    if 'PowerOriginal' not in data.columns:
        print("Die Spalte 'PowerOriginal' fehlt in den Daten.")
        return

    # Vorbereitung der Daten: Entfernen von fehlenden Werten und Sortieren
    power_data = data['PowerOriginal']
    sorted_power = bubble_sort(power_data.tolist())  # Die Daten sortieren
    sorted_power_reversed = sorted_power[::-1]  # Liste umkehren
    print(sorted_power_reversed)

    # Erstelle einen Ordner für die Grafiken, falls noch nicht vorhanden
    check_and_create_directory()

    # Daten visualisieren
    plot_data(sorted_power_reversed)

    print("Die Grafik wurde unter 'figures/power_curve.png' gespeichert.")

if __name__ == '__main__':
    main()
