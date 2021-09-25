def readFile():
    info = []
    with open("file.txt", 'r') as file:
        for line in file:
            for word in line.split():
                info.append(word)

    lines = int(info[0])
    columns = int(info[1])
    planner = [[info[l*columns+c+2]
                for c in range(columns)] for l in range(lines)]

    print(planner)


readFile()
