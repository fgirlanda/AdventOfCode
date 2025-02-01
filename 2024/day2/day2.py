def main():
    file_name = 'day2/input.txt'
    print(parte2(file_name))


def parte1(file_name):
    righe = leggi_file(file_name)
    validi = []

    for r in righe:
        if is_safe(riga_to_report(r)):
            validi.append(r)

    return len(validi)

def parte2(file_name):
    righe = leggi_file(file_name)
    validi = []

    for r in righe:
        if tolleranza(riga_to_report(r)):
            validi.append(r)

    return len(validi)

def leggi_file(file_name):
    with open(file_name) as f:
        righe = f.readlines()
        # reports = [list(map(int, riga.split())) for riga in righe]

    return righe

def riga_to_report(riga: str):
    report = list(map(int, riga.split()))

    return report 

def tolleranza(report: list[int]):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
        
    return False

def is_safe(report: list[int]):
    gradienti = [abs(x1 - x2) for x1, x2 in zip(report, report[1:])]

    if not all(x1 < x2 for x1,x2 in zip(report, report[1:])):
        if not all(x1 > x2 for x1,x2 in zip(report, report[1:])):
            return False
    if not all(1 <= g <= 3 for g in gradienti):
        return False
    
    return True
    
    

if __name__ == '__main__':
    main()