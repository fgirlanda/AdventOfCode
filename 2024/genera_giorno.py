import os
import requests
import sys
from apikeys import SESSION_ID

def crea_cartella(nome_cartella):
    if not os.path.exists(nome_cartella):
        os.makedirs(nome_cartella)


def crea_file_python(percorso_file):
    contenuto_python = f"""# Script per Advent of Code giorno {day_number}

def main():
    FILE_PATH = '2024/day{day_number}/esempio.txt'

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
        response = requests.get(url, cookies={"session": SESSION_ID})  # Sostituisci con la tua sessione AoC
        response.raise_for_status()
        with open(percorso_destinazione, "wb") as f:
            f.write(response.content)
        print(f"✅ File scaricato con successo: {percorso_destinazione}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Errore nel download del file: {e}")

if __name__ == "__main__":
    # Controlla se l'utente ha passato un numero di giorno
    if len(sys.argv) < 2:
        print("❌ Errore: Devi specificare il giorno come argomento!")
        print("Esempio: python script.py day8")
        sys.exit(1)

    # Prende il numero del giorno dall'argomento
    day_number = sys.argv[1][3:]

    # Definisce il nome della cartella e l'URL
    nome_cartella = f"day{day_number}"
    url_file = f"https://adventofcode.com/2024/day/{day_number}/input"

    # Creazione della cartella
    crea_cartella(nome_cartella)

    # Percorsi dei file
    percorso_python = os.path.join(nome_cartella, f"day{day_number}.py")
    percorso_esempio = os.path.join(nome_cartella, "esempio.txt")
    percorso_input = os.path.join(nome_cartella, "input.txt")

    # Creazione dei file
    crea_file_python(percorso_python)
    crea_file_vuoto(percorso_esempio)

    # Download dell'input
    scarica_file(url_file, percorso_input)

    print(f"📂 Cartella '{nome_cartella}' creata con i file necessari.")