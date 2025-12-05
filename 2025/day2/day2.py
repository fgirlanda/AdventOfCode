# Script per Advent of Code 2025 - giorno 2

def main():
    FILE_PATH = '2025/day2/input.txt'

    with open(FILE_PATH) as file:
        line = file.read()
        ranges = line.split(",")

    result1 = parte1(ranges)
    result2 = parte2(ranges)
    print("Parte 1: ", result1)
    print("\nParte2 : ", result2)
    

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

# def parte2(ranges):
#     sum = 0
#     for range in ranges:
#         temp = range.split("-")
#         start = int(temp[0])
#         end = int(temp[1])
#         invalidi = calcola_invalidi_2(start, end)
        
# def calcola_invalidi_2(start, end):
#     invalidi = []
#     for val in range(start, end+1):
#         str_val = str(val)
#         candidate = str_val[0]
#         repeat = 0
#         for i in range(1, len(str_val)):
#             current = str_val[i:len(candidate)]
#             if current == candidate:
#                 repeat+=1
#                 continue
#             elif current != candidate and True:
#                 candidate += current

def parte2(ranges):
    sum = 0
    for range in ranges:
        temp = range.split('-')
        start = int(temp[0])
        end = int(temp[1])
        invalidi = calcola_invalidi_2(start, end)
        for invalido in invalidi:
            sum += invalido
    return sum

# nota: + veloce partire da metà stringa (ancora + veloce con espressioni regolari)
def calcola_invalidi_2(start, end):
    invalidi = []
    for val in range(start, end+1):
        str_val = str(val)
        l = len(str_val)
        for i in range(1, (l//2)+1):
            sub = str_val[:i]
            occ = str_val.count(sub)
            if occ*len(sub) == l: 
                # print("val: ", val,"\nsub: ", sub, "\t\tocc: ", occ)
                invalidi.append(val)
                break
    return invalidi
            
            
# 123123123
# 123
            
            
                

if __name__ == "__main__":
    main()
