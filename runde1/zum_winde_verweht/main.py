import csv
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

with open("gebaeude.csv", newline='') as csvfile:
    buildings = list(csv.reader(csvfile))

with open("windraeder.csv", newline='') as csvfile:
     windWheels = list(csv.reader(csvfile))



for w in windWheels:
    min_dist = math.inf
    for b in buildings:
        curr_dist = distance(float(w[1]), float(w[2]), float(b[1]), float(b[2]))
        if (curr_dist < min_dist):
            min_dist = curr_dist
    w.append(min_dist / 10.0)
print(windWheels)


