import os
import requests
import sys
from apikeys import SESSION_ID


def crea_cartella(nome_cartella):
    if not os.path.exists(nome_cartella):
        os.makedirs(nome_cartella)


def crea_file_python(percorso_file, year, day_number):
    contenuto_python = f"""# Script per Advent of Code {year} - giorno {day_number}

def main():
    FILE_PATH = '{year}/day{day_number}/esempio.txt'

    with open(FILE_PATH) as file:
        pass

if __name__ == "__main__":
    main()
"""

    with open(percorso_file, 'w') as file:
        file.write(contenuto_python)


def crea_file_vuoto(percorso_file):
    open(percorso_file, "w").close()


def scarica_file(url, percorso_destinazione):
    try:
        response = requests.get(url, cookies={"session": SESSION_ID})
        response.raise_for_status()
        with open(percorso_destinazione, "wb") as f:
            f.write(response.content)
        print(f"✅ File scaricato con successo: {percorso_destinazione}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Errore nel download del file: {e}")


if __name__ == "__main__":
    # Controllo argomenti
    if len(sys.argv) < 3:
        print("❌ Devi specificare anno e giorno!")
        print("Esempio: python script.py 2025 day8")
        sys.exit(1)

    year = sys.argv[1]
    day_number = sys.argv[2][3:]  # rimuove 'day'

    # Percorso della cartella principale dell'anno
    year_folder = year
    crea_cartella(year_folder)

    # Cartella del giorno dentro l'anno
    nome_cartella = os.path.join(year_folder, f"day{day_number}")
    crea_cartella(nome_cartella)

    # URL input
    url_file = f"https://adventofcode.com/{year}/day/{day_number}/input"

    # Percorsi file
    percorso_python = os.path.join(nome_cartella, f"day{day_number}.py")
    percorso_esempio = os.path.join(nome_cartella, "esempio.txt")
    percorso_input = os.path.join(nome_cartella, "input.txt")

    # Creazione file locali
    crea_file_python(percorso_python, year, day_number)
    crea_file_vuoto(percorso_esempio)

    # Download dell’input
    scarica_file(url_file, percorso_input)

    print(f"📂 Cartella '{nome_cartella}' creata con i file necessari.")