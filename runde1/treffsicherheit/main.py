import math


def readFile():
    info = []
    with open("file.txt", 'r') as file:
        for line in file:
            for word in line.split():
                info.append(word)
    lines = int(info[0])
    columns = int(info[1])
    planner = [[info[l*columns+c+2] for l in range(lines)]
               for c in range(columns)]

    return(planner)


planner = readFile()
print(planner)


def isBestDate(t, p):
    for i in range(len(planner)):
        if int(planner[t][p]) > int(planner[i][p]):
            return False
    return True


bestDate = None
final_adjustments = math.inf
for t in range(len(planner)):
    adjustments = 0
    for p in range(len(planner[t])):
        if isBestDate(t, p) == False:
            adjustments += 1
    if adjustments < final_adjustments:
        final_adjustments = adjustments
        bestDate = t

print("bestDate", bestDate + 1, "number of adjustments", final_adjustments)
