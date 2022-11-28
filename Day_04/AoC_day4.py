# Advent of Code
# Day 4
# https://adventofcode.com/2021/day/4

file = open("input.txt", "r")
input = file.readlines()

random_pull = list(map(int, input[0].rstrip("\n").split(",")))

boards = []
for i in range(2, len(input), 6):
    tiles = input[i : i + 6]
    temp = []
    for tile in tiles:
        if tile != "\n":
            tile_row = tile.rstrip("\n").split(" ")
            numbers = []
            for i in tile_row:
                if i != "":
                    numbers.append(int(i))
            temp.append(numbers)
    boards.append(temp)


def check_for_bingo(board_number, row, column):
    number_of_marks = 0
    for i in range(5):
        if boards_marked[board_number][row][i] == "x":
            number_of_marks += 1
    if number_of_marks == 5:
        return True
    number_of_marks = 0
    for i in range(5):
        if boards_marked[board_number][i][column] == "x":
            number_of_marks += 1
    if number_of_marks == 5:
        return True
    return False


boards_marked = []
for i in range(len(boards)):
    list_j = []
    for j in range(5):
        list_l = []
        for l in range(5):
            list_l.append("")
        list_j.append(list_l)
    boards_marked.append(list_j)


def bingo():
    for number in random_pull:
        for i in range(len(boards)):
            for j in range(5):
                for l in range(5):
                    if boards[i][j][l] == number:
                        boards_marked[i][j][l] = "x"
                        if check_for_bingo(i, j, l):
                            return [i, j, l, number]


bingo_board, bingo_row, bingo_column, number = bingo()
sum = 0
for i in range(5):
    for j in range(5):
        if boards_marked[bingo_board][i][j] == "":
            sum += boards[bingo_board][i][j]
print("First Puzzle:", sum * number)


for i in range(len(boards)):
    for j in range(5):
        for l in range(5):
            boards_marked[i][j][l] = ""

boards_to_test = []
for i in range(len(boards)):
    boards_to_test.append(i)


def bingo2():
    winning_board = 0
    winning_number = 0
    for number in random_pull:
        for i in range(len(boards)):
            if boards_to_test.count(i) > 0:
                for j in range(5):
                    for l in range(5):
                        if boards[i][j][l] == number:
                            boards_marked[i][j][l] = "x"
                            if check_for_bingo(i, j, l):
                                winning_board = i
                                winning_number = number
                                boards_to_test.remove(i)
    return winning_board, winning_number


winning_board, winning_number = bingo2()
sum = 0
for i in range(5):
    for j in range(5):
        if boards_marked[winning_board][i][j] == "":
            sum += boards[winning_board][i][j]
print("Second Puzzle:", sum * winning_number)
