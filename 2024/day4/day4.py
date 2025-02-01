def main():
    print("Main")
    file_name = 'day4/input.txt'
    with open(file_name) as file:
        righe = [f for f in file]

    griglia = crea_griglia(righe) #1

    print(trova_x(griglia))

   
  
    # trova_parola(griglia)

#1) CREAZIONE GRIGLIA
def crea_griglia(righe):
    print("Creazione griglia")
    griglia = []
    
    for r in righe:
        r = r.rstrip('\n')
        lista_lettere = [c for c in r]
        griglia.append(lista_lettere)

    # CONTROLLO
    # for r in range(len(griglia)):
    #     print(griglia[r])
    
    return griglia

#2) CERCO X
def trova_x(griglia):
    totale = 0
    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if(griglia[r][c] == 'X'):
                totale += cerca_vicine_x(griglia, r, c)
    return totale           

    # print(coordinate)
    # return coordinate

#3) CERCO VICINE DELLA X
def cerca_vicine_x(griglia, rx, cx):
    totale_singola_x = 0

    for a,b in directions:
        new_r = rx + a
        new_c = cx + b
        if 0 <= new_r < len(griglia) and 0 <= new_c < len(griglia[0]):
            if griglia[new_r][new_c] == 'M':
                vicina = ((new_r, new_c), (a,b))
                totale_singola_x += cerca_direzione(griglia, vicina)

    return totale_singola_x           

def cerca_direzione(griglia, vicina):
    new_r = vicina[0][0] + vicina[1][0]
    new_c = vicina[0][1] + vicina[1][1]
    # print(vicina)
    if 0 <= new_r < len(griglia) and 0 <= new_c < len(griglia[0]):
        if griglia[new_r][new_c] == 'A':
                final_r, final_c = (new_r + vicina[1][0]), (new_c + vicina[1][1])
                if 0 <= final_r < len(griglia) and 0 <= final_c < len(griglia[0]):
                    if griglia[final_r][final_c] == 'S':
                        return 1
    return 0


# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....    



    

    


            

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1), (1, 0), (1, 1)]           

# def trova_parola(griglia):
#     trova_x(griglia)
#     #direction = cerca_vicine(griglia, rx, cx)

# def cerca_vicine(griglia, rx, cx):
#     vicine = [griglia[rx+a][cx+b] for a,b in directions]
#     print(vicine)
#     for vicina in vicine:
#         if vicina == 'M':
#             return directions.index(vicina)


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