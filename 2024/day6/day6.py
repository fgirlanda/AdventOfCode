def main():
    file_name = "AdventOfCode/2024/day6/input.txt"
    griglia = []
    with open(file_name) as file:
        griglia = [riga.strip() for riga in file]
        
    
    
    for riga in griglia:
        for elemento in riga:
            if elemento != '.' and elemento != '#':
                start_r = griglia.index(riga)
                start_c = riga.index(elemento)
    

    visitati = trova_percorso(griglia, start_r, start_c)
    print(visitati)


dir = [(-1, 0),(0, 1),(1, 0),(0, -1)] # up, left, right, down
    

def trova_percorso(griglia, r, c):
    i = 0
    # visitate = []
    visitate = [[r,c]]
    
    while(True):
        # print(dir[i][0], dir[i][1])
        r += dir[i][0]
        c += dir[i][1]

        if r >= len(griglia) or c >= len(griglia[0]) or r < 0 or c < 0:
            break

        if griglia[r][c] == "#":
            r -= dir[i][0]
            c -= dir[i][1]
            if i == 3:
                i = 0
            else:
                i += 1

        elif([r,c] not in visitate):
            visitate.append([r,c])

    print(visitate)
    return len(visitate)
    




if __name__ == "__main__":
    main()