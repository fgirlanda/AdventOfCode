# Script per Advent of Code giorno 9

def main():
    FILE_PATH = '2024/day9/input.txt'

    with open(FILE_PATH) as file:
        disk_map = file.read()

    parte1 = calcolo_parte1(disk_map)
    print(f'Parte 1: {parte1}')

    parte2 = calcolo_parte2(disk_map)
    print(f'Parte 2: {parte2}')


def calcolo_parte1(disk_map):
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
    
    return checksum

        
def calcolo_parte2(disk_map):
    dim_file = []
    dim_spazi_vuoti = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            dim_file.append(int(disk_map[i]))
        else:
            dim_spazi_vuoti.append(int(disk_map[i]))

    fd = len(dim_file) - 1
    s = 0
    id = 0
    checksum = 0
    file_aggiunti = set()

    while len(file_aggiunti) != len(dim_file):
        if s not in file_aggiunti:
            for _ in range(dim_file[s]):
                checksum += id*s
                id += 1
            file_aggiunti.add(s)
        else:
            id += dim_file[s]
        while dim_spazi_vuoti[s] != 0 and fd >= 0:
            if fd not in file_aggiunti:
                if dim_file[fd] <= dim_spazi_vuoti[s]:
                    for _ in range(dim_file[fd]):
                        checksum += id*fd
                        id += 1
                    file_aggiunti.add(fd)
                    dim_spazi_vuoti[s] -= dim_file[fd]
            fd -= 1
        
        if fd < 0:
            id += dim_spazi_vuoti[s]

        fd = len(dim_file) - 1
        s += 1
        

    return checksum


if __name__ == "__main__":
    main()
