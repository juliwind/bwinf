info = []
with open("file.txt", 'r') as file:
    for line in file:
        for word in line.split():
            info.append(word)

place = [0] * (ord(info[1]) - ord(info[0]) + 1)
i = 3
while (i < len(info)):
    place[int(info[i + 1])] = info[i]
    place[int(info[i + 1]) + 1] = info[i]
    i += 2


def main(x, final):
    if place[x] == 0:
        return True
    if (place[x-1] == place[x]):
        # LEFT
        moveUpLeft(x)
        moveRight(x, final)
    elif (place[x+1] == place[x]):
        # RIGHT
        moveLeft(x, final)
        moveUpRight(x)

def moveUpLeft(point):
    if point-2 > len(place):
        if place[point-2] == 0:
            place[point-2] = place[point]
            place[point] = 0
            return True
        else:
            if (moveUpLeft(point-2)) == False:
                return False
            else: moveUpLeft(point)

def moveUpRight(point):
    if point+2 < len(place):
        if place[point+2] == 0:
            place[point+2] = place[point]
            place[point] = 0
            return True
        else:
            if (moveUpRight(point+2)) == False:
                return False
            else: moveUpRight(point)

def moveLeft(point, final):
    if point - 2 > len(place):
        if place[point-2] == 0:
            place[point-2] = place[point]
            place[point-1] = place[point]
            place[point+1] = 0
            place[point] = 0
            return True
        elif final == False:
            if place[point - 1] == 0:
                return moveUpLeft(point)
        else:
            if moveLeft(point-2, False) == False:
                return False
            else: moveLeft(point-2, False)


def moveRight(point, final):
    if point + 2 < len(place):
        if place[point+2] == 0:
            place[point+2] = place[point]
            place[point+1] = place[point]
            place[point-1] = 0
            place[point] = 0
            return True
        elif final == False:
            if place[point+1] == 0:
                return moveUpRight(point)
        else:
            if moveRight(point+2, False) == False:
                return False
            else: moveRight(point+2, False)

i = 0
for x in place:
    curr_place = main(i, True)
    #print(curr_place)
    if curr_place:
        print(i)
    i += 1


print(place)