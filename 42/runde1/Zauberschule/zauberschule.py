class Node:
    def __init__(self, top, bottom, n, e, s, w):
        self.top = top
        self.bottom = bottom
        self.n = n
        self.e = e
        self.s = s
        self.w = w
    


def main():
    field, start, end, n, m = readFile()
    #print(field, start, end)
    graph = createGraph(field, n, m)
    solution = solve(field, start, end) 

def solve(field, start, end):
    return 0



def createGraph(field, d_n, d_m):
    for i in range(len(field)):
        for j in range(len(field[i])):
             for k in range(len(field[i][j])):
                #FEHLER!!!! WÄNDNE NOCH NICHT MITEINBEZOGEN
                if i == 0:
                     b = -1
                     t = 3
                elif i == 1:
                    b = 3
                    t = -1
                else: 
                    print("Falsche Eingabe! Keine 2 Stockwerke!")
                    exit()

                if j >= (d_n - 1):
                    n = 1
                    s = -1
                elif j <= 0:
                    n = -1
                    s = 1
                else:
                    n = 1
                    s = 1

                if k >= (d_m - 1):
                    e = -1
                    w = 1
                elif k <= 0:
                    e = 1
                    w = -1
                else:
                    e = 1
                    w = 1
                
                new_Node = Node(t, b, n, e, s, w)


        



def readFile() :
        # open the file
    with open('zauberschule0.txt') as f:
        # read all lines from the file
        lines = f.readlines()

    # Define global variables:
    stockwerk1 = []
    stockwerk2 = []
    dim_n = 0
    dim_m = 0
    start = [-1, -1, -1]
    end   = [-1, -1, -1]

    # Read the dimensions n and m:
    first_line = lines[0].split()
    dim_n = int(first_line[0])
    dim_m = int(first_line[1])

    #print ("Dim n = %d" % dim_n)
    #print ("Dim m = %d" % dim_m)

    # Read Stockwerk 1:
    for i in range(dim_n):
        stockwerk1.append(lines[i+1])

    # Check newline between Stockwerk 1 and 2;
    if lines[dim_n+1] != "\n":
        print ("FORMAT ERROR in INPUT FILE!")
        exit()

    # Read Stockwerk 2:
    for i in range(dim_n):
        stockwerk2.append(lines[i+dim_n+2])

    # Print Stockwerk1 and 2:
    #print("Stockwerk 1:")
    #for l in stockwerk1:
    #    print(l)
    #print("Stockwerk 2:")
    #for l in stockwerk2:
    #    print(l)

    # Find A (Start) and B (End)
    for i in range (dim_n):
        for j in range (dim_m):
            if stockwerk1[i][j] == 'A':
                start[0] = i
                start[1] = j
                start[2] = 1
            if stockwerk1[i][j] == 'B':
                end[0] = i
                end[1] = j
                end[2] = 1
            if stockwerk2[i][j] == 'A':
                start[0] = i
                start[1] = j
                start[2] = 2
            if stockwerk2[i][j] == 'B':
                end[0] = i
                end[1] = j
                end[2] = 2

    #print ("Start(A): ", start)
    #print ("End(B):   ", end)
    field = [stockwerk1, stockwerk2]
    print(field[0][9][5])
    return(field, start, end, dim_n, dim_m)



if __name__ == "__main__":
    main()