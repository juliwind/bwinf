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


def main(x):
    if place[x] == 0:
        return True
    if (place[x - 1] == place[x]):
        # LEFT
        moveLeft(x, 1)
        moveRight(x, 2)
    elif (place[x + 1] == place[x]):
        # RIGHT
        moveLeft(x, 2)
        moveRight(x, 1)


def moveLeft(point, step_number):
    car_name = place[point]
    place[point] = 0
    if step_number == 1:
        place[point - 2] = car_name
    else:
        place[point + 1] = 0
        place[point - 1] = car_name
        place[point - 2] = car_name


def moveRight(point, step_number):
    print()


i = 0
for x in place:
    main(i)
    print(i, "i")
    i += 1


print(place)
