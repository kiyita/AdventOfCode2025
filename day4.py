"""
Advent of Code Day 4 Solution
Author: Lucie
Date: 2025-12-04
Python 3
"""

import copy

# Part 1

def txtToList(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]

def lessThanFourAround(position, datas):
    x, y = position
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):  # Ignorer la position centrale
                if 0 <= x+i < len(datas) and 0 <= y+j < len(datas[0]):
                    if datas[x+i][y+j] == '@':
                        count += 1
    return count < 4
    

def solvingPart1(datas):
    total = 0
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            if datas[i][j] == '@':
                if lessThanFourAround((i, j), datas):
                    total += 1
    return total

# Part 2

def solvingPart2(datas):
    update = copy.deepcopy(datas)
    total = 0
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            if datas[i][j] == '@':
                if lessThanFourAround((i, j), datas):
                    total += 1
                    update[i][j] = 'x'
    if update == datas:
        return total
    else:
        return total + solvingPart2(update)
        

# Main Execution

def main():
    datas = txtToList("entry4.txt")
    part1_result = solvingPart1(datas)
    print("Part 1 Result:", part1_result)
    
    part2_result = solvingPart2(datas)
    print("Part 2 Result:", part2_result)

if __name__ == "__main__":
    main()
