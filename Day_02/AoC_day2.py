# Advent of Code
# Day 2
# https://adventofcode.com/2021/day/2

file = open("input.txt", "r")
input = file.readlines()


instr = []
for i in input:
    string = i.split(" ")
    integer = string[1].split("\\")
    instr.append([string[0], int(integer[0])])


depth = 0
horizontal = 0
for ins in instr:
    if ins[0] == "forward":
        horizontal += ins[1]
    elif ins[0] == "down":
        depth += ins[1]
    elif ins[0] == "up":
        depth -= ins[1]

print("First Puzzle:", depth * horizontal)


depth = 0
horizontal = 0
aim = 0
for ins in instr:
    if ins[0] == "forward":
        horizontal += ins[1]
        depth += aim * ins[1]
    elif ins[0] == "down":
        aim += ins[1]
    elif ins[0] == "up":
        aim -= ins[1]
print("Second Puzzle:", depth * horizontal)
