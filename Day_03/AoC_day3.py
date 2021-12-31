# Advent of Code
# Day 3
# https://adventofcode.com/2021/day/3

file = open("input.txt", "r")
input = file.readlines()

report = []
for i in input:
    report.append(i.strip("\n"))


count_0 = [0,0,0,0,0,0,0,0,0,0,0,0]
count_1 = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in report:
    for j in range(0, 12):
        if i[j] == "1":
            count_1[j] += 1
        else:
            count_0[j] += 1

bits = ""
inverted_bits = ""
for i in range(0, 12):
    if count_1[i] >= count_0[i]:
        bits += "1"
        inverted_bits += "0"
    else:
        bits += "0"
        inverted_bits += "1"
gamma_rate = int(bits, 2)
epsilon_rate = int(inverted_bits, 2)
print("First Puzzle:", gamma_rate * epsilon_rate)


list_for_oxygen_generator = report.copy()
list_for_CO2_scrubber = report.copy()
for i in range(0, 12):
    if count_1[i] >= count_0[i]:
        if len(list_for_oxygen_generator) > 1:
            temp_list = list_for_oxygen_generator.copy()
            for item in temp_list:
                if len(list_for_oxygen_generator) > 1:
                    if item[i] == "0":
                        list_for_oxygen_generator.remove(item)
        if len(list_for_CO2_scrubber) > 1:
            temp_list = list_for_CO2_scrubber.copy()
            for item in temp_list:
                if len(list_for_CO2_scrubber) > 1:
                    if item[i] == "1":
                        list_for_CO2_scrubber.remove(item)
    else:
        if len(list_for_oxygen_generator) > 1:
            temp_list = list_for_oxygen_generator.copy()
            for item in temp_list:
                if len(list_for_oxygen_generator) > 1:
                    if item[i] == "1":
                        list_for_oxygen_generator.remove(item)
        if len(list_for_CO2_scrubber) > 1:
            temp_list = list_for_CO2_scrubber.copy()
            for item in temp_list:
                if len(list_for_CO2_scrubber) > 1:
                    if item[i] == "0":
                        list_for_CO2_scrubber.remove(item)

oxygen_generator_rating = int(list_for_oxygen_generator[0], 2)
CO2_scrubber_rating = int(list_for_CO2_scrubber[0], 2)
print("Second Puzzle:", oxygen_generator_rating * CO2_scrubber_rating)
