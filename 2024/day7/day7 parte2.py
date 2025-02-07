def main():
    file_name = "2024/day7/input.txt"
    with open(file_name) as file:
        equazioni = dict()
        righe = file.readlines()
        for riga in righe:
            ris = int(riga.split(':')[0])
            operandi = [int(num) for num in riga.split(':')[1].strip().split(' ')]
            equazioni[ris] = operandi

    parte2 = 0
   
    for risultato, operandi in equazioni.items():
        if is_valid(operandi, risultato, operandi[0], 1):
                parte2 += risultato
                
    print(f"Parte 2: {parte2}")
    
def is_valid(operandi, risultato, valore_corrente, indice):
    if indice == len(operandi) or valore_corrente > risultato:
        return valore_corrente == risultato
    else:
        operandi_modificati = operandi[:indice-1]+[int(str(valore_corrente)+str(operandi[indice]))]+operandi[indice+1:]
        return (is_valid(operandi, risultato, valore_corrente + operandi[indice], indice + 1) or is_valid(operandi, risultato, valore_corrente * operandi[indice], indice + 1) or
                is_valid(operandi_modificati, risultato, int(str(valore_corrente)+str(operandi[indice])), indice)) 
                
             

if __name__ == "__main__":
    main()