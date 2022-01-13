v0 = [1, 1, 1, 0, 1, 1, 1]
v1 = [0, 0, 1, 0, 0, 1, 0]
v2 = [1, 0, 1, 1, 1, 0, 1]
v3 = [1, 0, 1, 1, 0, 1, 1]
v4 = [0, 1, 1, 1, 0, 1, 0]
v5 = [1, 1, 0, 1, 0, 1, 1]
v6 = [1, 1, 0, 1, 1, 1, 1]
v7 = [1, 0, 1, 0, 0, 1, 0]
v8 = [1, 1, 1, 1, 1, 1, 1]
v9 = [1, 1, 1, 1, 0, 1, 1]
va = [1, 1, 1, 1, 1, 1, 0]
vb = [0, 1, 0, 1, 1, 1, 1]
vc = [1, 1, 0, 0, 1, 0, 1]
vd = [0, 0, 1, 1, 1, 1, 1]
ve = [1, 1, 0, 1, 1, 0, 1]
vf = [1, 1, 0, 1, 1, 0, 0]

array_of_all = []
array_of_all.append(v0)
array_of_all.append(v1)
array_of_all.append(v2)
array_of_all.append(v3)
array_of_all.append(v4)
array_of_all.append(v5)
array_of_all.append(v6)
array_of_all.append(v7)
array_of_all.append(v8)
array_of_all.append(v9)
array_of_all.append(va)
array_of_all.append(vb)
array_of_all.append(vc)
array_of_all.append(vd)
array_of_all.append(ve)
array_of_all.append(vf)


def solve(array_from, array_to):
    additions = 0
    subtractions = 0
    for i in range(len(array_from)):
        if array_from[i] == 0 and array_to[i] == 1:
            additions += 1
        if array_from[i] == 1 and array_to[i] == 0:
            subtractions += 1
    return "additions", additions, "subtractions", subtractions


counter = 0
for i in array_of_all:
    for j in array_of_all:
        if i != j:
            counter += 1
            a_and_s = solve(i, j)
            print(a_and_s, counter)
