def readFile(p):
    info = []
    with open("file.txt", 'r') as file:
        for line in file:
            for word in line.split():
                info.append(word)

    p = [0] * (ord(info[1]) - ord(info[0]) + 1)
    i = 3
    while (i < len(info)):
        p[int(info[i + 1])] = info[i]
        p[int(info[i + 1]) + 1] = info[i]
        i += 2
    return (p)


def makeSpace(p, i):
    if i > (len(p) - 1):
        return False
    if p[i] == 0:
        return True
    if (moveRight1(p, i)):
        return True
    if (carLeftSide(p, i)):
        if (moveLeft2(p, i)):
            return True
        return False

    if (carRightSide(p, i)):
        if (moveLeft1(p, i)):
            return True
        if (moveRight2(p, i)):
            return True
    return False


def moveLeft2(p, i):  # i zeigt auf linken Teil vom Auto
    pp = p.copy()
    if i < 2:
        return False
    if p[i - 2] == 0 and p[i - 1] == 0:
        path.append(p[i] + " 2 links")
        return True
    if p[i-1] == 0 and p[i-2] != 0:
        if moveLeft1(pp, i-2):
            path.append(p[i] + " 2 links")
            return True
    if p[i-1] != 0 and p[i-2] != 0:
        if moveLeft2(pp, i-2):
            path.append(p[i] + " 2 links")
            return True
    return False


def moveLeft1(p, i):   # i zeigt auf den rechten Teil vom Auto
    pp = p.copy()
    if i < 1:
        return False
    if p[i-2] == 0:
        path.append(p[i] + " 1 links")
        return True
    else:
        if moveLeft1(pp, i-2):
            path.append(p[i] + " 1 links")
            return True
    return False


def moveRight2(p, i):     # i zeigt auf rechten Teil von Auto
    pp = p.copy()
    if i > (len(p) - 3):
        return False
    if p[i + 2] == 0 and p[i + 1] == 0:
        path.append(p[i] + " 2 rechts")
        return True
    if p[i + 1] == 0 and p[i + 2] != 0:
        if moveRight1(pp, i + 2):
            path.append(p[i] + " 2 rechts")
            return True
    if p[i + 1] != 0 and p[i + 2] != 0:
        if moveRight2(pp, i + 2):
            path.append(p[i] + " 2 rechts")
            return True
    return False


def moveRight1(p, i):   # i zeigt auf linken Teil von Auto
    pp = p.copy()
    if i > (len(p) - 3):
        return False
    if p[i+2] == 0:
        path.append(p[i] + " 1 rechts")
        return True
    else:
        if moveRight1(pp, i+2):
            path.append(p[i] + " 1 rechts")
            return True
    return False


def carLeftSide(p, i):
    if i >= len(p):
        return False
    if p[i] == 0:
        return False
    if i < (len(p) - 1) and p[i + 1] == p[i]:
        return True
    return False


def carRightSide(p, i):
    if i >= len(p):
        return False
    if p[i] == 0:
        return False
    if i > 0 and p[i - 1] == p[i]:
        return True
    return False


path = []
parking_place = []
parking_place = readFile(parking_place)

print(parking_place)

for i in range(len(parking_place)):
    path = []
    print("Freimachen: %d" % i)
    print(makeSpace(parking_place, i))
    print(path)
