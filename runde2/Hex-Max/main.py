import numpy as np
import math

input_path = 'resources\hexmax0.txt'

#s = subtraction
#a = addition
transformations = {
    "0": {"1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0}, "5": {"a": 0, "s": 0},
          "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "1": {"0": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0}, "5": {"a": 0, "s": 0},
          "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "2": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0}, "5": {"a": 0, "s": 0},
          "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "3": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0}, "5": {"a": 0, "s": 0},
          "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "4": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "5": {"a": 0, "s": 0},
          "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "5": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "6": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "7": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "8": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "9": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "a": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "a": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0},
          "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "b": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0},
          "a": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "c": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0},
          "a": {"a": 0, "s": 0}, "b": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "d": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0},
          "a": {"a": 0, "s": 0}, "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "e": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0},
          "a": {"a": 0, "s": 0}, "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "f": {"a": 0, "s": 0}},
    "f": {"0": {"a": 0, "s": 0}, "1": {"a": 0, "s": 0}, "2": {"a": 0, "s": 0}, "3": {"a": 0, "s": 0}, "4": {"a": 0, "s": 0},
          "5": {"a": 0, "s": 0}, "6": {"a": 0, "s": 0}, "7": {"a": 0, "s": 0}, "8": {"a": 0, "s": 0}, "9": {"a": 0, "s": 0},
          "a": {"a": 0, "s": 0}, "b": {"a": 0, "s": 0}, "c": {"a": 0, "s": 0}, "d": {"a": 0, "s": 0}, "e": {"a": 0, "s": 0}}
}
hex_numbers = ["f", "e", "d", "c", "b", "a", 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def readFile():
    input_hex = []
    with open(input_path, 'r') as file:
        for letter in file.readline():
            input_hex.append(letter.rstrip())
        max_shifts = file.readline().rstrip()
    input_hex = [x for x in input_hex if x != '']
    for i in range(len(input_hex)):
        input_hex[i] = input_hex[i].lower()

    return input_hex, max_shifts


class Digit:


hex, max_shifts = readFile()
# print("hex", hex, "max shifts", max_shifts)
print(transformations["b"]["c"])