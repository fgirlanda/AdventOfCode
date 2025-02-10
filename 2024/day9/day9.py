# Script per Advent of Code giorno 9

def main():
    FILE_PATH = '2024/day9/esempio.txt'

    with open(FILE_PATH) as file:
        disk_map = file.read()
        print(disk_map)

    rappresentazione = ""
    id = 0

    for i in range(len(disk_map)):
        if i % 2 == 0:
            rappresentazione += str(id)*int(disk_map[i])
            id += 1
        else:
            rappresentazione += '.'*int(disk_map[i])
    
    print(rappresentazione)
    
    #TO DO - Ottimizzare (troppo lento)
    for dx in range(len(rappresentazione) -1 , -1, -1):
        if rappresentazione[dx] != '.':
            tmp_char = rappresentazione[dx]
            rappresentazione = rappresentazione[:dx] + '.' + rappresentazione[dx+1:]
            for sx in range(len(rappresentazione)):
                if rappresentazione[sx] == '.':
                    rappresentazione = rappresentazione[:sx] + tmp_char + rappresentazione[sx+1:]
                    print(rappresentazione)
                    break



if __name__ == "__main__":
    main()
