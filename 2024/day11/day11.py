# Script per Advent of Code giorno 11

def main():
    FILE_PATH = '2024/day11/input.txt'

    with open(FILE_PATH) as file:
        stones = list(map(int, file.readline().split(" ")))
        print(stones)
    
    parte1 = final_stones(stones)

    print(f'Parte 1: {len(parte1)}')

def final_stones(stones):
    for _ in range(25):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                num = str(stones[i])
                val1 = int(num[:len(num)//2])
                val2 = int(num[len(num)//2:])
                stones[i:i+1] = [val1, val2]
                i += 1
            else:
                stones[i] *= 2024
            i += 1
    
    return stones
    




if __name__ == "__main__":
    main()
