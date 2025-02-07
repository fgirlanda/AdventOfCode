def main():
    file_name = "2024/day7/input.txt"
    with open(file_name) as file:
        equazioni = dict()
        righe = file.readlines()
        for riga in righe:
            ris = int(riga.split(':')[0])
            operandi = [int(num) for num in riga.split(':')[1].strip().split(' ')]
            equazioni[ris] = operandi

    parte1 = 0
    validi1 = dict()

    for risultato, operandi in equazioni.items():
        if is_valid(operandi, risultato, operandi[0], 1):
                parte1 += risultato
                validi1[risultato] = operandi
    
    print(f"Parte 1: {parte1}")
    
def is_valid(operandi, risultato, valore_corrente, indice):
    if indice == len(operandi):
        return valore_corrente == risultato
    else:
        return is_valid(operandi, risultato, valore_corrente + operandi[indice], indice + 1) or is_valid(operandi, risultato, valore_corrente * operandi[indice], indice + 1)
             
        

if __name__ == "__main__":
    main()