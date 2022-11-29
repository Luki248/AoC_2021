# Advent of Code
# Day 5
# https://adventofcode.com/2021/day/5

file = open("input.txt", "r")
input = file.readlines()

lines = []
for row in input:
    row = row.strip("\n").split(" -> ")
    temp1 = row[0].split(",")
    temp2 = row[1].split(",")
    lines.append([int(temp1[0]), int(temp1[1]), int(temp2[0]), int(temp2[1])])

map = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    map.append(row)

for line in lines:
    x1, y1, x2, y2 = line
    if x1 == x2 or y1 == y2:
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                map[y][x] += 1

sum = 0
for i in range(1000):
    for j in range(1000):
        if map[i][j] >= 2:
            sum += 1

print("First Puzzle:", sum)


print("Second Puzzle:")
