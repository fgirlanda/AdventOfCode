# Script per Advent of Code 2025 - giorno 3

def main():
    FILE_PATH = '2025/day3/input.txt'

    with open(FILE_PATH) as file:
        banks = []
        for bank in file:
            bank = bank.strip()
            banks.append(bank)
    
    result1 = parte1(banks)
    result2 = parte2(banks) # Corretto: 3121910778619

    print("Parte1: ", result1, "\nParte2: ", result2)

def parte1(banks):
    res = 0
    for bank in banks:
        res += calcola_joltage(bank)
        
    return res

        
                
def calcola_joltage(bank: str):
    coppie = []
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            coppia = bank[i] + bank[j]
            if coppia not in coppie: coppie.append(coppia)
    
    coppia_max = 0
    for coppia in coppie:
        val_coppia = int(coppia)
        if val_coppia >= coppia_max:
            coppia_max = val_coppia
    return coppia_max

def parte2(banks):
    somma = 0
    for bank in banks:
        somma += calcola_joltage_2(bank)

    return somma

def calcola_joltage_2(bank: str):
    
    joltage = ''
    pos_iniziale = 0
    for k in range(12):
        current_max = int(bank[pos_iniziale])
        max_pos = pos_iniziale
        for i in range(pos_iniziale+1, len(bank)-(11-k)):
            if int(bank[i]) > current_max:
                current_max = int(bank[i])
                max_pos = i
                
                
        joltage += str(current_max)
        pos_iniziale = max_pos + 1
        # pos_iniziale = bank.index(str(current_max)) + 1

    return int(joltage)




    
        
        
if __name__ == "__main__":
    main()
