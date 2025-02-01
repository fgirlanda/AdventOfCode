def main():
    file_name = "AdventOfCode/2024/day6/esempio.txt"
    griglia = []
    with open(file_name) as file:
        griglia = [riga.strip() for riga in file]
        
    num_r = len(griglia)
    num_c = len(griglia[0])

    for i in range(num_r):
        for j in range(num_c):
            if griglia[i][j] == '.':
                griglia[i][j] = '#'
    print(griglia)
dir = [(-1, 0), (0, +1), ()]  
def check_loop(griglia, r, c):
    start_r = r
    start_c = c


                



if __name__ == "__main__":
    main()