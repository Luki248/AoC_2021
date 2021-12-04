# Advent of Code
# Day 1
# https://adventofcode.com/2021/day/1

file = open("input.txt", "r")
input = file.readlines()

depths = []
for i in input:
    depths.append(int(i))

count = 0
for i in range(len(depths) - 1):
    if depths[i+1] > depths[i]:
        count += 1
print("First Puzzle:", count)


count = 0
last = depths[0] + depths[1] + depths[2]
for i in range(1, len(depths) - 2):
    sum = depths[i] + depths[i+1] + depths[i+2]
    if sum > last:
        count += 1
    last = sum
print("Second Puzzle:", count)
