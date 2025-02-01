from collections import defaultdict
import re

def main():
    file_name = "AdventOfCode/2024/day5/input.txt"
    parte1 = 0
    parte2 = 0

    with open(file_name) as file:
        testo = file.read()
        mappa_regole = crea_mappa(testo)
        updates = crea_lista_update(testo)
        # print(updates)
    
    # lista_prio = genera_lista_prio(mappa_regole)
    for update in updates:
        if is_ordinato1(update, mappa_regole):
            parte1 += update[int(len(update)/2)]
        else:
            parte2 += centrale_riordinato(update, mappa_regole)
            
    
    print(f'Parte 1: {parte1}')
    print(f'Parte 2: {parte2}')
    

#GENERA MAPPA_REGOLE E LISTA_UPDATE  
def crea_mappa(testo):
    regola_key = r'(\d+)\|(\d+)'

    stringhe_mappa_regole = re.findall(regola_key, testo)
    mappa_regole = [[int(x),int(y)] for x,y in stringhe_mappa_regole]

    return mappa_regole


def crea_lista_update(testo):
    updates = []

    for riga in testo.splitlines():
        riga.strip()
        if "|" not in riga and testo.index(riga) > 0:
            updates.append(list(map(int, re.findall(r'\d+', riga))))

    return updates

#PARTE 1
def is_ordinato1(update, mappa_regole):
    for x,y in mappa_regole:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False         
    return True

#PARTE2
def centrale_riordinato(update, mappa_regole):
    mappa_regole_custom = []
    for x,y in mappa_regole:
        if x in update and y in update:
            mappa_regole_custom.append([x,y])

    # print(update, mappa_regole_custom)
    lista_prio = genera_lista_prio(mappa_regole_custom)
    # print(lista_prio)
    ordinato = riordina_update(update, lista_prio)

    return ordinato[int(len(ordinato)/2)]
         
    
def riordina_update(update, prio):
    stack = []
    visited = [0]*len(prio)

    for num in update:
        if visited[num] == 0:
            dfs(num, visited, prio, stack)
    
    return stack[::-1]

def dfs(node, visited, prio, stack):
    visited[node] = 1

    for prev in prio[node]:
        if visited[prev] == 0:
            dfs(prev, visited, prio, stack)
    if node not in stack:
        stack.append(node)
    

def genera_lista_prio(mappa_regole):
    dizionario_lista_prio = defaultdict(list)
    indice_max = 0
    lista_prio = []

    for x,y in mappa_regole:
        dizionario_lista_prio[x].append(y)
        indice_max = max(indice_max, x, y)
    for i in range(indice_max + 2):
        if i in dizionario_lista_prio:
            lista_prio.append(dizionario_lista_prio[i])
        else:
            lista_prio.append([])
    
    return lista_prio 

if __name__ == '__main__':
    main()

