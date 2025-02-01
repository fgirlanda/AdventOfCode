def main():
    print("Main")
    file_name = 'AdventOfCode/2024/day4/input.txt'
    with open(file_name) as file:
        righe = [f for f in file]

    griglia = crea_griglia(righe) #1

    print(trova_x(griglia))


#1) CREAZIONE GRIGLIA
def crea_griglia(righe):
    print("Creazione griglia")
    griglia = []
    
    for r in righe:
        r = r.rstrip('\n')
        lista_lettere = [c for c in r]
        griglia.append(lista_lettere)

    
    return griglia

#2) CERCO X
def trova_x(griglia):
    totale = 0
    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if(griglia[r][c] == 'X'):
                totale += trova_parola(griglia, r, c)
    return totale 

def trova_parola(griglia, rx, cx):
    parola = 'MAS'
    conta_parole = 0

    for a,b in directions:
        new_r = rx
        new_c = cx
        for step in range(len(parola)):
            new_r += a
            new_c += b
            if 0 <= new_r < len(griglia) and 0 <= new_c < len(griglia[0]):
                if(griglia[new_r][new_c] != parola[step]):
                    break
                elif(step == len(parola) - 1):
                    conta_parole += 1
            else:
                break
                  
             
    return conta_parole           


      


directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1), (1, 0), (1, 1)]           


if __name__ == "__main__":
    main()




# ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M']
# ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A']
# ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M']
# ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X']
# ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M']
# ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A']
# ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S']
# ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A']
# ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M']
# ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']