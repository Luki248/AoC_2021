# Advent of Code
# Day 3
# https://adventofcode.com/2021/day/3

file = open("input.txt", "r")
input = file.readlines()

report = []
for i in input:
    report.append(i.strip("\n"))


count_zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in report:
    for j in range(0, 12):
        if i[j] == "1":
            count_ones[j] += 1
        else:
            count_zeros[j] += 1

bits = ""
inverted_bits = ""
for i in range(0, 12):
    if count_ones[i] >= count_zeros[i]:
        bits += "1"
        inverted_bits += "0"
    else:
        bits += "0"
        inverted_bits += "1"
gamma_rate = int(bits, 2)
epsilon_rate = int(inverted_bits, 2)
print("First Puzzle:", gamma_rate * epsilon_rate)


list_for_oxygen = report.copy()
for i in range(0, 12):
    if len(list_for_oxygen) > 1:
        count_ones = 0
        count_zeros = 0
        for item in list_for_oxygen:
            if item[i] == "1":
                count_ones += 1
            else:
                count_zeros += 1

        temp = list_for_oxygen.copy()
        if count_ones >= count_zeros:
            for item in temp:
                if item[i] == "0":
                    list_for_oxygen.remove(item)
        else:
            for item in temp:
                if item[i] == "1":
                    list_for_oxygen.remove(item)

list_for_CO2 = report.copy()
for i in range(0, 12):
    if len(list_for_CO2) > 1:
        count_ones = 0
        count_zeros = 0
        for item in list_for_CO2:
            if item[i] == "1":
                count_ones += 1
            else:
                count_zeros += 1

        temp = list_for_CO2.copy()
        if count_ones >= count_zeros:
            for item in temp:
                if item[i] == "1":
                    list_for_CO2.remove(item)
        else:
            for item in temp:
                if item[i] == "0":
                    list_for_CO2.remove(item)

oxygen_generator_rating = int(list_for_oxygen[0], 2)
CO2_scrubber_rating = int(list_for_CO2[0], 2)
print("Second Puzzle:", oxygen_generator_rating * CO2_scrubber_rating)
