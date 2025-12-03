"""
Advent of Code Day 3 Solution
Author: Lucie
Date: 2025-12-03
Python 3
"""

# Part 1

def txtToList(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def solvingPart1(datas):
    total = 0
    for line in datas:
        max = (0, 0) #max and its place in line
        for i in range(len(line)):
            if int(line[i]) > max[0]:
                max = (int(line[i]), i)
        if max[1] == len(line) - 1: #if it's the last number, must me the second one
            max2 = 0
            for j in range(len(line) - 1):
                if int(line[j]) > max2:
                    max2 = int(line[j])
            total += int(str(max2) + str(max[0]))
        else:
            max2 = 0
            for j in range(max[1] + 1, len(line)):
                if (int(line[j]) > max2):
                    max2 = int(line[j])
            total += int(str(max[0]) + str(max2))
    return total

# Part 2

def solvingPart2(datas):
    total = 0
    for line in datas:
        max = [(0, 0) for _ in range(12)] #max and its place in line
        numberToAdd = ""
        for k in range(12):
            for i in range(max[k-1][1], int(len(line) - 11 + k)):
                if int(line[i]) > max[k][0] and i not in [max[m][1] for m in range(k)]:
                    max[k] = (int(line[i]), i)
            numberToAdd += str(max[k][0])
        print(numberToAdd)
        total += int(numberToAdd)
    return total
        

# Main Execution

def main():
    datas = txtToList("entry3.txt")
    part1_result = solvingPart1(datas)
    print("Part 1 Result:", part1_result)
    
    part2_result = solvingPart2(datas)
    print("Part 2 Result:", part2_result)

if __name__ == "__main__":
    main()
