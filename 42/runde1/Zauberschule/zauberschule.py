class Node:
    def __init__(self, top, bottom, n, e, s, w):
        self.top = top
        self.bottom = bottom
        self.n = n
        self.e = e
        self.s = s
        self.w = w
    
    def show(self):
        print("Top: ", self.top, " Bottom: ", self.bottom, " N: ", self.n, " E: ", self.e, " S: ", self.s, " W: ", self.w)


def main():
    field, start, end, n, m = readFile()
    graph = createGraph(field, n, m)
    solution = solve(graph, start, end) 

def solve(graph, start, end):
    first_node = graph[start[2]][start[0]][start[1]]
    first_node.show()

def createGraph(field, d_n, d_m):
    graph = [[],[]]
    for i in range(len(field[0]) - 1):
        graph[0].append([])
        graph[1].append([])
        for j in range(len(field[0][i]) - 1):
            graph[0][i].append(0)
            graph[1][i].append(0)

    for i in range(len(field)):
        for j in range(len(field[i]) - 1):
             for k in range(len(field[i][j]) - 1):
                if i == 0:
                    b = -1
                    if field[1][j][k] == "." or field[1][j][k] == "A" or field[1][j][k] == "B": 
                        t = 3
                    elif field[1][j][k] == "#":
                        t = -1
                    else:
                        exit()
                elif i == 1:
                    t = -1
                    if field[0][j][k] == "." or field[0][j][k] == "A" or field[0][j][k] == "B":
                        b = 3
                    elif field[0][j][k] == "#":
                        b = -1
                    else: 
                        exit()
                else:
                    exit()
                if j >= (d_n - 1):
                    s = -1
                    if field[i][j-1][k] == "." or field[i][j-1][k] == "A" or field[i][j-1][k] == "B":
                        n = 1
                    elif field[i][j-1][k] == "#":
                        n = -1
                    else: 
                        exit()
                elif j <= 0:
                    n = -1
                    if field[i][j+1][k] == "." or field[i][j+1][k] == "A" or field[i][j+1][k] == "B":
                        s = 1
                    elif field[i][j+1][k] == "#":
                        s = -1
                    else: 
                        exit()
                else:
                    if field[i][j-1][k] == "." or field[i][j-1][k] == "A" or field[i][j-1][k] == "B":
                        n = 1
                    elif field[i][j-1][k] == "#":
                        n = -1
                    else: 
                        exit()
                    if field[i][j+1][k] == "." or field[i][j+1][k] == "A" or field[i][j+1][k] == "B":
                        s = 1
                    elif field[i][j+1][k] == "#":
                        s = -1
                    else: 
                        exit()
                if k >= (d_m - 1):
                    e = -1
                    if field[i][j][k-1] == "." or field[i][j][k-1] == "A" or field[i][j][k-1] == "B":
                        w = 1
                    elif field[i][j][k-1] == "#":
                        w = -1
                    else: 
                        exit()
                elif k <= 0:
                    w = -1
                    if field[i][j][k+1] == "." or field[i][j][k+1] == "A" or field[i][j][k+1] == "B":
                        e = 1
                    elif field[i][j][k+1] == "#":
                        e = -1
                    else: 
                        exit()
                else: 
                    if field[i][j][k-1] == "." or field[i][j][k-1] == "A" or field[i][j][k-1] == "B":
                        w = 1
                    elif field[i][j][k-1] == "#":
                        w = -1
                    else: 
                        exit()
                    if field[i][j][k+1] == "." or field[i][j][k+1] == "A" or field[i][j][k+1] == "B":
                        e = 1
                    elif field[i][j][k+1] == "#":
                        e = -1
                    else: 
                        exit()
                new_Node = Node(t, b, n, e, s, w)
                graph[i][j][k] = new_Node

    return graph
                     


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

    # Read Stockwerk 1:
    for i in range(dim_n):
        stockwerk1.append(lines[i+1])

    # Check newline between Stockwerk 1 and 2;
    if lines[dim_n+1] != "\n":
        exit()

    # Read Stockwerk 2:
    for i in range(dim_n):
        stockwerk2.append(lines[i+dim_n+2])

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

    field = [stockwerk1, stockwerk2]
    return(field, start, end, dim_n, dim_m)



if __name__ == "__main__":
    main()