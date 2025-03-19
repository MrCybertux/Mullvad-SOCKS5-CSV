import json
import wget
import csv

# Die URL der JSON-Datei von Mullvad
url = "https://api.mullvad.net/public/relays/wireguard/v1/"

# Lade die JSON-Datei herunter
response = wget.download(url, "mullvad_servers.json")

# Lade die JSON-Daten aus der Datei
with open("mullvad_servers.json", "r") as f:
    data = json.load(f)

# Extrahiere die Hostnamen und formatiere sie gemäß dem gewünschten Schema
formatted_hostnames = []
for country in data.get("countries", []):
    for city in country.get("cities", []):
        for relay in city.get("relays", []):
            hostname = relay.get("hostname", "")
            # Formatieren des Hostnamens gemäß dem Schema
            if "wg" in hostname:
                # Einfügen von '-socks5' zwischen 'wg' und der Nummer
                parts = hostname.split("-wg-")
                formatted_hostname = f"{parts[0]}-wg-socks5-{parts[1]}.relays.mullvad.net"
                
                # Extrahiere das Länderkürzel aus dem Hostnamen (vor dem ersten '-')
                country_code = hostname.split("-")[0]
                
                formatted_hostnames.append([country_code, formatted_hostname])

# Schreibe die Daten in eine CSV-Datei
with open("mullvad_hostnames.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Country Code", "Hostname"])  # Header-Zeile
    writer.writerows(formatted_hostnames)

print("CSV-Datei 'mullvad_hostnames.csv' wurde erstellt.")

