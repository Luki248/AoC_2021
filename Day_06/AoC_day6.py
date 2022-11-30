# Advent of Code
# Day 6
# https://adventofcode.com/2021/day/6

file = open("input.txt", "r")
input = file.readlines()

fishes = [int(i) for i in input[0].split(",")]
fishes_copy = fishes.copy()
for _ in range(80):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes_copy[i] = 6
            fishes_copy.append(8)
        else:
            fishes_copy[i] -= 1
    fishes = fishes_copy.copy()

print("First Puzzle:", len(fishes))


fishes = [int(i) for i in input[0].split(",")]
fishes_copy = fishes.copy()
for _ in range(256):
    print("\r", _, end="")
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes_copy[i] = 6
            fishes_copy.append(8)
        else:
            fishes_copy[i] -= 1
    fishes = fishes_copy.copy()

print("\rSecond Puzzle:", len(fishes))
