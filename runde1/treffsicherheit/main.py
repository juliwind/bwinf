import math


def readFile():
    info = []
    with open("file.txt", 'r') as file:
        for line in file:
            for word in line.split():
                info.append(word)
    # planner = [[0 for l in range(int(info[0]))]for c in range(int(info[1]))]
    lines = int(info[0])
    columns = int(info[1])
    planner = [[info[l*columns+c+2] for l in range(lines)]
               for c in range(columns)]

    return(planner)


planner = readFile()
print(planner)
# planner[T][P]


def isBestDate(t, p):
    if int(planner[t][p]) == 0:
        return True
    else:
        return False
#        for i in t:
#            if int(t) > int(t):
#                return False
#        return True
#    return False


bestDate = None
final_adjustments = math.inf
for t in range(len(planner)):   # geht alle termine durch
    adjustments = 0
    for p in range(len(planner[t])):     # geht alle personen durch
        if isBestDate(t, p) == False:
            # p = 0
            adjustments += 1
    if adjustments < final_adjustments:
        final_adjustments = adjustments
        bestDate = t


print("bestDate", bestDate, "number of adjustments", final_adjustments)


# [['0', '1', '2', '2', '0', '1'], TERMIN 1
# ['0', '0', '2', '1', '1', '2'], TERMIN 2
# ['0', '0', '2', '1', '2', '1'], TERMIN 3
# ['0', '1', '1', '1', '2', '2'], TERMIN 4
# ['0', '1', '2', '2', '1', '0'], TERMIN 5
# ['0', '0', '2', '1', '0', '1'], TERMIN 6
# ['0', '0', '2', '2', '0', '1']] TERMIN 7

#   1    2    3    4    5    6
# PERSON PERSON PERSON PERSON PERSON PERSON
