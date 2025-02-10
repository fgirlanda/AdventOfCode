# Script per Advent of Code giorno 9

def main():
    FILE_PATH = '2024/day9/input.txt'

    with open(FILE_PATH) as file:
        disk_map = file.read()

    print(disk_map)
    dx = len(disk_map) - 1
    sx = 0
    cont = 0
    checksum = 0
    while sx <= dx:
        if sx % 2 == 0:
            for _ in range(int(disk_map[sx])):
                checksum += (sx//2) * cont
                cont += 1
            sx += 1
        else:
            for _ in range(min(int(disk_map[dx]), int(disk_map[sx]))):
                checksum += (dx//2) * cont
                cont += 1
                disk_map = disk_map[:dx] + str((int(disk_map[dx]) - 1)) + disk_map[dx+1:]
                disk_map = disk_map[:sx] + str((int(disk_map[sx]) - 1)) + disk_map[sx+1:]
            if disk_map[dx] == '0':
                dx -= 2
            if disk_map[sx] == '0':
                sx += 1
        # print(disk_map)
    
    print(checksum)
        



if __name__ == "__main__":
    main()
