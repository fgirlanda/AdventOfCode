def main():
    file_name = "AdventOfCode/2024/day7/esempio.txt"
    with open(file_name) as file:
        risultati = []
        operandi = []
        for riga in file:
            riga = riga.strip()
            riga = riga.split(':')
            risultati.append(riga[0])
            operandi.append(list(map(int, riga[1].split())))
        # print(risultati)
        # print(operandi)    
    for ris in risultati:
        for i in range(len(operandi.index(ris))):
            tmp = 
        

if __name__ == "__main__":
    main()