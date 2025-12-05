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
    
    start = 50
    result1 = parte1(istruzioni, start)
    result2 = parte2(istruzioni, start)
    result2_alt = parte2_alt(istruzioni, start)
    print("Parte 1 : ", result1, 
          "\nParte 2:", result2,
          "\nParte 2 alt:", result2_alt)
    
def parte1(istruzioni, start):
    result = 0
    temp = start
    for istruzione in istruzioni:
        if istruzione[0] == 'L':
            temp -= istruzione[1]
        else:
            temp += istruzione[1]
        temp = temp%100
        if temp == 0:
            result += 1
            
    return result

def parte2_alt(istruzioni, start):
    # PROBLEMA = non conta passaggi multipli dallo 0 + 
    # result = 0
    # temp = start
    # prev = temp
    # for istruzione in istruzioni:
    #     if istruzione[0] == 'L':
    #         temp -= istruzione[1]
    #     else:
    #         temp += istruzione[1]
            
        
    #     if temp != temp%100 and prev != 0:
    #         result += 1
        
    #     temp = temp%100
    #     prev = temp

    # return result
    
    # VERSIONE CORRETTA
    result = 0
    temp = start
    
    for istruzione in istruzioni:
        if istruzione[0] == 'L':
            nuovo = temp - istruzione[1]
            # Attraversamenti andando a sinistra
            result += (temp - 1) // 100 - (nuovo - 1) // 100
        else:
            nuovo = temp + istruzione[1]
            # Attraversamenti andando a destra
            result += nuovo // 100 - temp // 100
        
        temp = nuovo % 100
    

def parte2(istruzioni, start):
    result = 0
    temp = start
    for istruzione in istruzioni:
        if istruzione[0] == 'L':
            for _ in range(istruzione[1]):
                if temp == 0:
                    temp = 99
                    if _ != 0: result += 1
                    continue
                temp -= 1
        else:
            for _ in range(istruzione[1]):
                if temp == 99:
                    temp = 0
                    result += 1
                    continue
                temp += 1
            
    return result

                
            
                

if __name__ == "__main__":
    main()
