# Script per Advent of Code giorno 8

def main():
    #creazione griglia
    FILE_PATH = '2024/day8/input.txt'

    with open(FILE_PATH) as file:
        griglia = [list(riga.strip()) for riga in file.readlines()]
    
    antinodi_parte1 = []
    antinodi_parte2 = []

    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if griglia[r][c] != '.':
                antinodi_carattere_parte1 = calcola_antinodi_parte1(griglia[r][c], griglia, r, c)
                antinodi_carattere_parte2 = calcola_antinodi_parte2(griglia[r][c], griglia, r, c)
                for antinodo1 in antinodi_carattere_parte1:
                    if antinodo1 not in antinodi_parte1:
                        antinodi_parte1.append(antinodo1)
                for antinodo2 in antinodi_carattere_parte2:
                    if antinodo2 not in antinodi_parte2:
                        antinodi_parte2.append(antinodo2)
                    
    print(f'Parte 1: {len(antinodi_parte1)}')
    print(f'Parte 2: {len(antinodi_parte2)}')

def calcola_antinodi_parte1(char, griglia, start_r, start_c):
    antinodi_locale = [(start_r, start_c)]

    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if griglia[r][c] == char:
                #calcolo coordinate antinodi 
                r_a1 = start_r - (r-start_r)
                c_a1 = start_c - (c-start_c)
                r_a2 = r + (r-start_r)
                c_a2 = c + (c-start_c)
                if controllo_bordi(r_a1, c_a1, griglia) and (r_a1, c_a1) not in antinodi_locale:
                    antinodi_locale.append((r_a1, c_a1))   
                if controllo_bordi(r_a2, c_a2, griglia) and (r_a2, c_a2) not in antinodi_locale:
                    antinodi_locale.append((r_a2, c_a2))
                    
    antinodi_locale.remove((start_r, start_c))

    return antinodi_locale


def calcola_antinodi_parte2(char, griglia, start_r, start_c):
    antinodi_locale = [(start_r, start_c)]

    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if griglia[r][c] == char:
                for i in range(len(griglia)):
                    r_a1 = start_r - (i*(r-start_r))
                    c_a1 = start_c - (i*(c-start_c))
                    r_a2 = r + (i*(r-start_r))
                    c_a2 = c + (i*(c-start_c))
                    if controllo_bordi(r_a1, c_a1, griglia) and (r_a1, c_a1) not in antinodi_locale:
                        antinodi_locale.append((r_a1, c_a1))   
                    if controllo_bordi(r_a2, c_a2, griglia) and (r_a2, c_a2) not in antinodi_locale:
                        antinodi_locale.append((r_a2, c_a2))

    return antinodi_locale

def controllo_bordi(r, c, griglia):
    return 0 <= r < len(griglia) and 0 <= c < len(griglia[0])

if __name__ == "__main__":
    main()
