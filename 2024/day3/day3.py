import re

def main():
    file_name = 'day3/input.txt'

    with open(file_name) as f:
        testo_completo = f.read()

    print(f"Parte 1: {parte1(testo_completo)}")
    print(f"Parte 2: {parte2(testo_completo)}")


def parte1(stringa):
    key = r'mul\((\d{1,3}),(\d{1,3})\)'
    totale = 0

    coppie = re.findall(key, stringa)
    coppie = [(int(x), int(y)) for x,y in coppie]
    totale += sum(x*y for x,y in coppie)

    return totale
        

def parte2(stringa):
    part2 = 0
    enabled = True

    for inst in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", stringa):
        match inst:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                x , y = map(int, inst[4:-1].split(','))
                if enabled:
                    part2 += x * y
    return part2

    

if __name__ == '__main__':
    main()