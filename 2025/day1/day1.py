# Script per Advent of Code 2025 - giorno 1

def main():
    FILE_PATH = '2025/day1/input.txt'

    with open(FILE_PATH) as file:
        istruzioni = []
        for riga in file:
            riga = riga.strip()
            direction = riga[0]
            valore = int(riga[1:])
            istruzioni.append((direction, valore))
        
    result = parte1(istruzioni)
    print(result)

def parte1(istruzioni):
    start = 50
    result = 0
    temp = start
    for istruzione in istruzioni:
        if istruzione[0] == 'L':
            for _ in range(istruzione[1]):
                if temp == 0:
                    temp = 99
                    continue
                temp -= 1
        else:
            for _ in range(istruzione[1]):
                if temp == 99:
                    temp = 0
                    continue
                temp += 1
        if temp == 0:
                result += 1
            
    return result
                
            
                

if __name__ == "__main__":
    main()
