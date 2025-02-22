# Script per Advent of Code giorno 10
from collections import deque

def main():
    FILE_PATH = '2024/day10/input.txt'

    with open(FILE_PATH) as file:
        griglia = [list(map(int, riga.strip())) for riga in file]

    parte1 = 0
    parte2 = 0
    zeri = set()

    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if griglia[r][c] == 0:
                zeri.add((r,c))
    
    print(len(zeri))
    
    for (r, c) in zeri:
        nove = calcola_score(griglia, r, c)
        parte1 += len(nove)
        parte2 += calcola_rating(griglia, r, c)
    
    print(f'Parte 1: {parte1}')
    print(f'Parte 2: {parte2}')
             
def calcola_score(griglia, r, c):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([(r, c)]) 
    visitati = set((r,c))
    nove_trovati = set()

    while queue:
        x, y = queue.popleft()
        valore_corrente = griglia[x][y]

        for dx, dy in directions:
            nx, ny, = x + dx, y + dy

            if in_bound(griglia, nx, ny) and (nx, ny) not in visitati:
                prossimo_valore = griglia[nx][ny]
                if prossimo_valore == valore_corrente + 1:
                    visitati.add((nx,ny))
                    queue.append((nx,ny))
                    if prossimo_valore == 9:
                        nove_trovati.add((nx,ny))
    
    return nove_trovati

def calcola_rating(griglia, r, c):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([(r, c)]) 
    paths = 0

    while queue:
        x, y = queue.popleft()

        if griglia[x][y] == 9:
            paths += 1
            continue

        for dr, dc in directions:
            nr, nc = x + dr, y + dc
            if in_bound(griglia, nr, nc) and griglia[nr][nc] == griglia[x][y] + 1:
                queue.append((nr, nc))

    return paths



def in_bound(griglia, r, c):
    return 0 <= r < len(griglia) and 0 <= c < len(griglia[0])





if __name__ == "__main__":
    main()
