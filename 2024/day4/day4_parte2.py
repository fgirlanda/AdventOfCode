def main():
    file_name = 'AdventOfCode/2024/day4/input.txt'
    with open(file_name) as file:
        righe = [f for f in file]

    griglia = crea_griglia(righe) #1
    print(trova_a(griglia))


#1) CREAZIONE GRIGLIA
def crea_griglia(righe):
    print("Creazione griglia")
    griglia = []
    
    for r in righe:
        r = r.rstrip('\n')
        lista_lettere = [c for c in r]
        griglia.append(lista_lettere)

    
    return griglia


#2) CERCO A
def trova_a(griglia):
    totale = 0
    parola = "MAS"
    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if(griglia[r][c] == parola[1]):
                totale += controlla_diagonali(griglia, r, c, parola)
    return totale 


#3) CONTROLLO DIAGONALI

def controlla_diagonali(griglia, ra, ca, parola):
    diag1 = ""
    diag2 = ""

    for a,b in diagonali:
        start_r = ra + (int(len(parola)/2))*a
        start_c = ca + (int(len(parola)/2))*b
        if not (0 <= start_r < len(griglia) and 0 <= start_c < len(griglia[0])):
            return 0
        else:
            for step in range(len(parola)):
                if a == 1:
                    diag1 += griglia[start_r - step][start_c - step]
                elif a == -1:
                    diag2 += griglia[start_r + step][start_c - step]
            
            if (diag1 == "SAM" or diag1 == "MAS") and (diag2 == "SAM" or diag2 == "MAS"):
                return 1
        
    return 0


                    


            

diagonali = [(1, 1), (-1, 1)]

if __name__ == "__main__":
    main()

