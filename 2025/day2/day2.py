# Script per Advent of Code 2025 - giorno 2

def main():
    FILE_PATH = '2025/day2/input.txt'

    with open(FILE_PATH) as file:
        line = file.read()
        ranges = line.split(",")

    result1 = parte1(ranges)
    print("Parte 1: ", result1)
    

def parte1(ranges):
    sum = 0
    for range in ranges:
        temp = range.split('-')
        start = int(temp[0])
        end = int(temp[1])
        # print(start, "-", end)
        invalidi = calcola_invalidi(start, end)
        for invalido in invalidi:
            sum += invalido
    return sum
        
def calcola_invalidi(start, end):
    invalidi = []
    for val in range (start, end+1):
        str_val = str(val)
        first_half = str_val[:len(str_val)//2]
        second_half = str_val[len(str_val)//2:]
        if(first_half == second_half):
            invalidi.append(val)
            # print(val)
    return invalidi

if __name__ == "__main__":
    main()
