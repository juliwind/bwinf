from utils import *

input_path = 'resources\hexmax0.txt'

# s = subtraction
# a = addition
all_hex = ['f', 'e', 'd', 'c', 'b', 'a', '9',
           '8', '7', '6', '5', '4', '3', '2', '1', '0']
transformations = {
    '0': {'1': {'a': 0, 's': 4}, '2': {'a': 1, 's': 2}, '3': {'a': 1, 's': 2}, '4': {'a': 1, 's': 3}, '5': {'a': 1, 's': 2},
          '6': {'a': 1, 's': 1}, '7': {'a': 0, 's': 3}, '8': {'a': 1, 's': 0}, '9': {'a': 1, 's': 1}, 'a': {'a': 1, 's': 1},
          'b': {'a': 1, 's': 2}, 'c': {'a': 0, 's': 2}, 'd': {'a': 1, 's': 2}, 'e': {'a': 1, 's': 2}, 'f': {'a': 1, 's': 3}},
    '1': {'0': {'a': 4, 's': 0}, '2': {'a': 4, 's': 1}, '3': {'a': 3, 's': 0}, '4': {'a': 2, 's': 0}, '5': {'a': 4, 's': 0},
          '6': {'a': 5, 's': 1}, '7': {'a': 1, 's': 0}, '8': {'a': 5, 's': 0}, '9': {'a': 4, 's': 0}, 'a': {'a': 4, 's': 0},
          'b': {'a': 4, 's': 1}, 'c': {'a': 4, 's': 2}, 'd': {'a': 3, 's': 0}, 'e': {'a': 5, 's': 2}, 'f': {'a': 4, 's': 2}},
    '2': {'0': {'a': 2, 's': 1}, '1': {'a': 1, 's': 4}, '3': {'a': 1, 's': 1}, '4': {'a': 2, 's': 3}, '5': {'a': 2, 's': 2},
          '6': {'a': 2, 's': 1}, '7': {'a': 1, 's': 3}, '8': {'a': 2, 's': 0}, '9': {'a': 2, 's': 1}, 'a': {'a': 2, 's': 1},
          'b': {'a': 2, 's': 2}, 'c': {'a': 1, 's': 2}, 'd': {'a': 1, 's': 1}, 'e': {'a': 1, 's': 1}, 'f': {'a': 1, 's': 2}},
    '3': {'0': {'a': 2, 's': 1}, '1': {'a': 0, 's': 3}, '2': {'a': 1, 's': 1}, '4': {'a': 1, 's': 2}, '5': {'a': 1, 's': 1},
          '6': {'a': 2, 's': 1}, '7': {'a': 0, 's': 2}, '8': {'a': 2, 's': 0}, '9': {'a': 1, 's': 0}, 'a': {'a': 2, 's': 1},
          'b': {'a': 2, 's': 2}, 'c': {'a': 2, 's': 3}, 'd': {'a': 1, 's': 1}, 'e': {'a': 2, 's': 2}, 'f': {'a': 2, 's': 3}},
    '4': {'0': {'a': 3, 's': 1}, '1': {'a': 0, 's': 2}, '2': {'a': 3, 's': 2}, '3': {'a': 2, 's': 1}, '5': {'a': 2, 's': 1},
          '6': {'a': 3, 's': 1}, '7': {'a': 1, 's': 2}, '8': {'a': 3, 's': 0}, '9': {'a': 2, 's': 0}, 'a': {'a': 2, 's': 0},
          'b': {'a': 2, 's': 1}, 'c': {'a': 3, 's': 3}, 'd': {'a': 2, 's': 1}, 'e': {'a': 3, 's': 2}, 'f': {'a': 2, 's': 2}},
    '5': {'0': {'a': 2, 's': 1}, '1': {'a': 1, 's': 4}, '2': {'a': 2, 's': 2}, '3': {'a': 1, 's': 1}, '4': {'a': 1, 's': 2},
          '6': {'a': 1, 's': 0}, '7': {'a': 1, 's': 3}, '8': {'a': 2, 's': 0}, '9': {'a': 1, 's': 0}, 'a': {'a': 2, 's': 1},
          'b': {'a': 1, 's': 1}, 'c': {'a': 1, 's': 2}, 'd': {'a': 2, 's': 2}, 'e': {'a': 1, 's': 1}, 'f': {'a': 1, 's': 2}},
    '6': {'0': {'a': 1, 's': 1}, '1': {'a': 1, 's': 5}, '2': {'a': 1, 's': 2}, '3': {'a': 1, 's': 2}, '4': {'a': 1, 's': 3},
          '5': {'a': 0, 's': 1}, '7': {'a': 1, 's': 4}, '8': {'a': 1, 's': 0}, '9': {'a': 1, 's': 1}, 'a': {'a': 1, 's': 1},
          'b': {'a': 0, 's': 1}, 'c': {'a': 0, 's': 2}, 'd': {'a': 1, 's': 2}, 'e': {'a': 0, 's': 1}, 'f': {'a': 0, 's': 2}},
    '7': {'0': {'a': 3, 's': 0}, '1': {'a': 0, 's': 1}, '2': {'a': 3, 's': 1}, '3': {'a': 2, 's': 0}, '4': {'a': 2, 's': 1},
          '5': {'a': 3, 's': 1}, '6': {'a': 4, 's': 1}, '8': {'a': 4, 's': 0}, '9': {'a': 3, 's': 0}, 'a': {'a': 3, 's': 0},
          'b': {'a': 4, 's': 2}, 'c': {'a': 3, 's': 2}, 'd': {'a': 3, 's': 1}, 'e': {'a': 4, 's': 2}, 'f': {'a': 3, 's': 2}},
    '8': {'0': {'a': 0, 's': 1}, '1': {'a': 0, 's': 5}, '2': {'a': 0, 's': 2}, '3': {'a': 0, 's': 2}, '4': {'a': 0, 's': 3},
          '5': {'a': 0, 's': 2}, '6': {'a': 0, 's': 1}, '7': {'a': 0, 's': 4}, '9': {'a': 0, 's': 1}, 'a': {'a': 0, 's': 1},
          'b': {'a': 0, 's': 2}, 'c': {'a': 0, 's': 3}, 'd': {'a': 0, 's': 2}, 'e': {'a': 0, 's': 2}, 'f': {'a': 0, 's': 3}},
    '9': {'0': {'a': 1, 's': 1}, '1': {'a': 0, 's': 4}, '2': {'a': 1, 's': 2}, '3': {'a': 0, 's': 1}, '4': {'a': 0, 's': 2},
          '5': {'a': 0, 's': 1}, '6': {'a': 1, 's': 1}, '7': {'a': 0, 's': 3}, '8': {'a': 1, 's': 0}, 'a': {'a': 1, 's': 1},
          'b': {'a': 1, 's': 2}, 'c': {'a': 1, 's': 3}, 'd': {'a': 1, 's': 2}, 'e': {'a': 1, 's': 2}, 'f': {'a': 1, 's': 3}},
    'a': {'0': {'a': 1, 's': 1}, '1': {'a': 0, 's': 4}, '2': {'a': 1, 's': 2}, '3': {'a': 1, 's': 2}, '4': {'a': 0, 's': 2},
          '5': {'a': 1, 's': 2}, '6': {'a': 1, 's': 1}, '7': {'a': 0, 's': 3}, '8': {'a': 1, 's': 0}, '9': {'a': 1, 's': 1},
          'b': {'a': 1, 's': 2}, 'c': {'a': 1, 's': 3}, 'd': {'a': 1, 's': 2}, 'e': {'a': 1, 's': 2}, 'f': {'a': 0, 's': 2}},
    'b': {'0': {'a': 2, 's': 1}, '1': {'a': 1, 's': 4}, '2': {'a': 2, 's': 2}, '3': {'a': 2, 's': 2}, '4': {'a': 1, 's': 2},
          '5': {'a': 1, 's': 1}, '6': {'a': 1, 's': 0}, '7': {'a': 2, 's': 4}, '8': {'a': 2, 's': 0}, '9': {'a': 2, 's': 1},
          'a': {'a': 2, 's': 1}, 'c': {'a': 1, 's': 2}, 'd': {'a': 1, 's': 1}, 'e': {'a': 1, 's': 1}, 'f': {'a': 1, 's': 2}},
    'c': {'0': {'a': 2, 's': 0}, '1': {'a': 2, 's': 4}, '2': {'a': 2, 's': 1}, '3': {'a': 3, 's': 2}, '4': {'a': 3, 's': 3},
          '5': {'a': 2, 's': 1}, '6': {'a': 2, 's': 0}, '7': {'a': 2, 's': 3}, '8': {'a': 3, 's': 0}, '9': {'a': 3, 's': 1},
          'a': {'a': 3, 's': 1}, 'b': {'a': 2, 's': 1}, 'd': {'a': 3, 's': 2}, 'e': {'a': 1, 's': 0}, 'f': {'a': 1, 's': 1}},
    'd': {'0': {'a': 2, 's': 1}, '1': {'a': 0, 's': 3}, '2': {'a': 1, 's': 1}, '3': {'a': 1, 's': 1}, '4': {'a': 1, 's': 2},
          '5': {'a': 2, 's': 2}, '6': {'a': 2, 's': 1}, '7': {'a': 1, 's': 3}, '8': {'a': 2, 's': 0}, '9': {'a': 2, 's': 1},
          'a': {'a': 2, 's': 1}, 'b': {'a': 1, 's': 1}, 'c': {'a': 2, 's': 3}, 'e': {'a': 2, 's': 2}, 'f': {'a': 2, 's': 3}},
    'e': {'0': {'a': 2, 's': 1}, '1': {'a': 2, 's': 5}, '2': {'a': 1, 's': 1}, '3': {'a': 2, 's': 2}, '4': {'a': 2, 's': 3},
          '5': {'a': 1, 's': 1}, '6': {'a': 1, 's': 0}, '7': {'a': 2, 's': 4}, '8': {'a': 2, 's': 0}, '9': {'a': 2, 's': 1},
          'a': {'a': 2, 's': 1}, 'b': {'a': 1, 's': 1}, 'c': {'a': 0, 's': 1}, 'd': {'a': 2, 's': 2}, 'f': {'a': 0, 's': 1}},
    'f': {'0': {'a': 3, 's': 1}, '1': {'a': 2, 's': 4}, '2': {'a': 2, 's': 1}, '3': {'a': 3, 's': 2}, '4': {'a': 2, 's': 2},
          '5': {'a': 2, 's': 1}, '6': {'a': 2, 's': 0}, '7': {'a': 2, 's': 3}, '8': {'a': 3, 's': 0}, '9': {'a': 3, 's': 1},
          'a': {'a': 2, 's': 0}, 'b': {'a': 2, 's': 1}, 'c': {'a': 1, 's': 1}, 'd': {'a': 3, 's': 2}, 'e': {'a': 1, 's': 0}}
}


def readFile():
    input_hex = []
    with open(input_path, 'r') as file:
        for letter in file.readline():
            input_hex.append(letter.rstrip())
        max_shifts = file.readline().rstrip()
        input_hex = [x for x in input_hex if x != '']
    for i in range(len(input_hex)):
        input_hex[i] = input_hex[i].lower()
    input_digits = []
    for i in input_hex:
        input_digits = makeObject(i, input_digits)
    return(input_digits, max_shifts)


def makeObject(x, array):
    match x:
        case '0':
            array.append(Digit('0', 1, 1, 1, 0, 1, 1, 1))
        case '1':
            array.append(Digit('1', 0, 0, 1, 0, 0, 1, 0))
        case '2':
            array.append(Digit('2', 1, 0, 1, 1, 1, 0, 1))
        case '3':
            array.append(Digit('3', 1, 0, 1, 1, 0, 1, 1))
        case '4':
            array.append(Digit('4', 0, 1, 1, 1, 0, 1, 0))
        case '5':
            array.append(Digit('5', 1, 1, 0, 1, 0, 1, 1))
        case '6':
            array.append(Digit('6', 1, 1, 0, 1, 1, 1, 1))
        case '7':
            array.append(Digit('7', 1, 0, 1, 0, 0, 1, 0))
        case '8':
            array.append(Digit('8', 1, 1, 1, 1, 1, 1, 1))
        case '9':
            array.append(Digit('9', 1, 1, 1, 1, 0, 1, 1))
        case 'a':
            array.append(Digit('a', 1, 1, 1, 1, 1, 1, 0))
        case 'b':
            array.append(Digit('b', 0, 1, 0, 1, 1, 1, 1))
        case 'c':
            array.append(Digit('c', 1, 1, 0, 0, 1, 0, 1))
        case 'd':
            array.append(Digit('d', 0, 0, 1, 1, 1, 1, 1))
        case 'e':
            array.append(Digit('e', 1, 1, 0, 1, 1, 0, 1))
        case 'f':
            array.append(Digit('f', 1, 1, 0, 1, 1, 0, 0))
    return array


# bei segmenten in der klasse digit: 0 = aus, 1 = ein, 2 = markierung: addition benötigt -> es muss etwas hinzugefügt werden, 3 = markierung: subtraktion benötigt: es muss etwas abegzogen werden


class Digit():
    def __init__(self, number, segment1, segment2, segment3, segment4, segment5, segment6, segment7):
        self.number = number
        self.segment1 = segment1
        self.segment2 = segment2
        self.segment3 = segment3
        self.segment4 = segment4
        self.segment5 = segment5
        self.segment6 = segment6
        self.segment7 = segment7

    def __repr__(self):
        return 'Number: ' + str(self.number) + ', Segment1: ' + str(self.segment1) + ', Segment2: ' + str(self.segment2) + ', Segment3: ' + str(self.segment3) + ', Segment4: ' + str(self.segment4) + ', Segment5: ' + str(self.segment5) + ', Segment6: ' + str(self.segment6) + ', Segment7: ' + str(self.segment7)

    def getSegment(self, x):
        string = "segment" + str(x)
        return getattr(self, string)

    def setSegment(self, x, value):
        string = "segment" + str(x)
        setattr(self, string, value)


#####################################
hex, shifts = readFile()
hex_changes = hex
open_moves = {'a': 0, 's': 0}

for c in range(len(hex)):
    i = hex[c]
    cur_number = i.number
    for j in all_hex:

        if cur_number < j:

            cur_a, cur_s = transformations[i.number][j]['a'], transformations[i.number][j]['s']
            print("from: ", i, "to: ", j, "additions: ",
                  cur_a, "subtractions: ", cur_s, "shifts: ", shifts)
            if enoughMovesLeft(open_moves['a'], open_moves['s'], cur_a, cur_s, shifts):
                print("enough moves left")
                # print("1: enoughMovesLeft = True, a: ", cur_a, "s: ", cur_s, "Transformation: from: ", i, "to: ", j)

                var_array = calcOutsideMoves(
                    cur_a, cur_s, open_moves['a'], open_moves['s'])
                a_outside, s_outside, open_moves['a'], open_moves['s'], cur_a, cur_s = var_array[
                    0], var_array[1], var_array[2], var_array[3], var_array[4], var_array[5]

                digit_transformation = makeObject(j, [])[0]
                seg_changes = generateChanges(i, digit_transformation)
                dig_changes = Digit(j, seg_changes[0], seg_changes[1], seg_changes[2],
                                    seg_changes[3], seg_changes[4], seg_changes[5], seg_changes[6])
                hex_changes.append(dig_changes)

                if a_outside > s_outside:
                    var_array = moveOutside(
                        "a", a_outside, hex, dig_changes, i, cur_a, cur_s)
                else:
                    var_array = moveOutside(
                        "s", s_outside, hex, dig_changes, i, cur_a, cur_s)

                int_shifts = int(shifts)
                int_shifts -= var_array[0]
                shifts = str(int_shifts)
                dig_changes, i, cur_a, cur_s = var_array[1], var_array[2], var_array[3], var_array[4]
                hex[c] = i
                hex_changes[c] = dig_changes

                # nun die 2 Fälle
                if cur_s == cur_a:
                    var_array = moveInside(
                        digit_transformation, dig_changes, cur_a, cur_s)
                    #print(shifts, var_array, "asdasd")
                    int_shifts = int(shifts)
                    int_shifts -= var_array
                    shifts = str(int_shifts)
                else:
                    var_array = moveInside(
                        digit_transformation, dig_changes, cur_a, cur_s)
                    int_shifts = int(shifts)
                    int_shifts -= var_array[0]
                    shifts = str(int_shifts)
                    cur_a, cur_s, dig_changes, i = var_array[1], var_array[2], var_array[3], var_array[4]
                    hex[c] = i
                    hex_changes[c] = dig_changes
                #print(dig_changes, shifts)

# 1. verschieben nach außen, wo benötigt ist
# 2. verschieben mit sich selber
# 3. rest notieren
# print("finished")
