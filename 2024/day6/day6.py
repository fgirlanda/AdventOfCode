def main():
    file_name = "2024/day6/input.txt"
    griglia = []
    with open(file_name) as file:
        griglia = [list(riga.strip()) for riga in file]
        
    nuovi_ostacoli = 0
    
    for riga in griglia:
        for elemento in riga:
            if elemento != '.' and elemento != '#':
                start_r = griglia.index(riga)
                start_c = riga.index(elemento)
    
    visitati = trova_percorso(griglia, start_r, start_c)
    print(f"Parte 1: {len(visitati)}")

    for r,c in visitati[1:]:
        griglia[r][c] = '#'
        if check_loop(griglia, start_r, start_c):
            # print(r,c)
            nuovi_ostacoli += 1
        griglia[r][c] = '.'

    print(f"Parte 2: {nuovi_ostacoli}")


# dir = [(-1, 0),(0, 1),(1, 0),(0, -1)] # up, right, down, left  

def trova_percorso(griglia, r, c):
    visitate = [[r,c]]
    dr = -1
    dc = 0
    
    while(True):
        r += dr
        c += dc

        if r >= len(griglia) or c >= len(griglia[0]) or r < 0 or c < 0:
            break

        if griglia[r][c] == "#":
            r -= dr
            c -= dc
            dr, dc = dc, -dr
            
           
        elif([r,c] not in visitate):
            visitate.append([r,c])
    
    # print(visitate)
    return visitate
    
def check_loop(griglia, r, c):
    visitate_up = [[r,c]]
    dr = -1
    dc = 0

    while(True):
        r += dr
        c += dc

        if dr == -1 and dc == 0:
            if [r,c] in visitate_up:
                return True
            else:
                visitate_up.append([r,c])
            
        if r >= len(griglia) or c >= len(griglia[0]) or r < 0 or c < 0:
            return False

        if griglia[r][c] == "#":
            r -= dr
            c -= dc
            dr, dc = dc, -dr




if __name__ == "__main__":
    main()