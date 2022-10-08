import math

buildings = []
windwheels = []


def readFile():
    info = []
    with open("file.txt", 'r') as file:
        for line in file:
            for word in line.split():
                info.append(int(word))
    n = info[0]
    m = info[1]
    for i in range(2, n*2+2, 2):
        new_building = []
        new_building.append(info[i])
        new_building.append(info[i+1])
        buildings.append(new_building)

    for i in range(n*2+2, 2*(n+m)+2, 2):
        new_windwheel = []
        new_windwheel.append(info[i])
        new_windwheel.append(info[i+1])
        windwheels.append(new_windwheel)


readFile()


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


for w in windwheels:
    min_dist = math.inf
    for b in buildings:
        curr_dist = distance(float(w[0]), float(
            w[1]), float(b[0]), float(b[1]))
        if (curr_dist < min_dist):
            min_dist = curr_dist
    w.append(min_dist / 10.0)
print(windwheels)
