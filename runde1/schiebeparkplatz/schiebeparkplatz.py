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
    return (p, info[0])


def makeSpace(p, i):
    if i > (len(p) - 1) or i < 0:
        return False, []
    if p[i] == 0:
        return True, []
    ret = False
    ret_left = False
    ret_right = False
    path_left = []
    path_right = []
    final_path = []

    if (carLeftSide(p, i)):
        if (moveRight1(p, i, path_right)):
            ret = True
            ret_right = True
            final_path = path_right
        if (moveLeft2(p, i, path_left)):
            ret = True
            ret_left = True
            final_path = path_left
        if (ret_right and ret_left):
            if (len(path_left) < len(path_right)):
                final_path = path_left
            else:
                final_path = path_right
        return ret, final_path

    if (carRightSide(p, i)):
        if (moveLeft1(p, i, path_left)):
            ret = True
            ret_left = True
            final_path = path_left
        if (moveRight2(p, i, path_right)):
            ret = True
            ret_right = True
            final_path = path_right
        if (ret_right and ret_left):
            if (len(path_left) < len(path_right)):
                final_path = path_left
            else:
                final_path = path_right
        return ret, final_path


def moveLeft2(p, i, path):  # i zeigt auf linken Teil vom Auto
    pp = p.copy()
    if i < 2:
        return False
    if p[i - 2] == 0 and p[i - 1] == 0:
        path.append(p[i] + " 2 links")
        return True, path
    if p[i-1] == 0 and p[i-2] != 0:
        if moveLeft1(pp, i-2, path):
            path.append(p[i] + " 2 links")
            return True, path
    if p[i-1] != 0 and p[i-2] != 0:
        if moveLeft2(pp, i-2, path):
            path.append(p[i] + " 2 links")
            return True, path
    return False


def moveLeft1(p, i, path):   # i zeigt auf den rechten Teil vom Auto
    pp = p.copy()
    if i < 1:
        return False
    if p[i-2] == 0:
        path.append(p[i] + " 1 links")
        return True, path
    else:
        if moveLeft1(pp, i-2, path):
            path.append(p[i] + " 1 links")
            return True, path
    return False


def moveRight2(p, i, path):     # i zeigt auf rechten Teil von Auto
    pp = p.copy()
    if i > (len(p) - 3):
        return False
    if p[i + 2] == 0 and p[i + 1] == 0:
        path.append(p[i] + " 2 rechts")
        return True, path
    if p[i + 1] == 0 and p[i + 2] != 0:
        if moveRight1(pp, i + 2, path):
            path.append(p[i] + " 2 rechts")
            return True, path
    if p[i + 1] != 0 and p[i + 2] != 0:
        if moveRight2(pp, i + 2, path):
            path.append(p[i] + " 2 rechts")
            return True, path
    return False


def moveRight1(p, i, path):   # i zeigt auf linken Teil von Auto
    pp = p.copy()
    if i > (len(p) - 3):
        return False
    if p[i+2] == 0:
        path.append(p[i] + " 1 rechts")
        return True, path
    else:
        if moveRight1(pp, i+2, path):
            path.append(p[i] + " 1 rechts")
            return True, path
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


parking_place = []
parking_place = readFile(parking_place)[0]
first_letter = ord(readFile(parking_place)[1])

for i in range(len(parking_place)):
    solution = makeSpace(parking_place, i)
    if (solution[0]):
        # print(solution[1])
        #print("%s:" % solution[1])
        print("%c: %s" % (chr(first_letter + i), ', '.join(solution[1])))
    else:
        print("%c: nicht moeglich!" % chr(first_letter + i))
