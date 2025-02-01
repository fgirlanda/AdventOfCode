from collections import defaultdict
import re

def main():
    file_name = "AdventOfCode/2024/day5/esempio.txt"
    updates = []

    with open(file_name) as file:
        testo_regole = file.read()
        mappa_regole = crea_mappa(testo_regole)
    with open(file_name) as file:
        testo_update = file.readlines()
        for i in range(len(mappa_regole) + 1, len(testo_update)):
            update = list(map(int, testo_update[i].split(',')))
            # print(update)
            updates.append(update)

    print(f"Numero update (corretto: {1361-1178+1})", len(updates))
    lista_prio = genera_lista_prio(mappa_regole)
    print(lista_prio)
    ordine = genera_ordine(lista_prio)
    # print(ordine)
    print(verifica_e_somma(ordine, updates))  
    

def crea_mappa(testo_regole):
    regola_key = r'(\d+)\|(\d+)'

    stringhe_mappa_regole = re.findall(regola_key, testo_regole)
    mappa_regole = [[int(x),int(y)] for x,y in stringhe_mappa_regole]

    return mappa_regole


def genera_lista_prio(mappa_regole):
    dizionario_lista_prio = defaultdict(list)
    indice_max = 0
    lista_prio = []

    for x,y in mappa_regole:
        dizionario_lista_prio[x].append(y)
        indice_max = max(indice_max, x)
    for i in range(indice_max + 2):
        if i in dizionario_lista_prio:
            lista_prio.append(dizionario_lista_prio[i])
        else:
            lista_prio.append([])
    
    return lista_prio


stack = []


def genera_ordine(lista_prio):
    visited = [0]*len(lista_prio)

    for i in range(len(lista_prio)):
        if visited[i] == 0:
            dfs(i, visited, lista_prio)
    
    ordine = stack[::-1]

    return ordine


def dfs(node, visited, prio):
    visited[node] = 1
    
    for j in prio[node]:
        if visited[j] == 0:
            dfs(j, visited, prio)

    if node not in stack:
        stack.append(node)


def verifica_e_somma(ordine, updates):
    somma = 0
    for update in updates:
        mapped_update = [(ordine.index(num), num) for num in update]
        print(update, mapped_update)
        #DEBUG
        # for i in range(len(update) - 1):
        #     print(mapped_update[i][0], mapped_update[i+1][0])

        if all(mapped_update[i][0] <= mapped_update[i+1][0] for i in range(len(update) - 1)):
            # print("entrato")

            somma += update[int(len(update)/2)]

        #ALTERNATIVA
        # sorted_update = sorted(mapped_update)
        # print(mapped_update, sorted_update)
        # if mapped_update == sorted_update:
        #     print("entrato")
        #     print(update)
        #     print(update[int(len(update)/2)])
        #     somma += update[int(len(update)/2)]
            
    return somma


if __name__ == "__main__":
    main()