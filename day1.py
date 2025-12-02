"""
Advent of Code Day 1 Solution
Author: Lucie
Date: 2025-12-01
Python 3
"""

# Part 1

def txtToList(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def solvingPart1():
    data = txtToList('entry1.txt')
    zeroCount = 0
    current = 50
    for move in data:
        if move[0] == 'L':
            current -= int(move[1:])
            current = current%100
        elif move[0] == 'R':
            current += int(move[1:])
            current = current%100
        if current == 0:
            zeroCount += 1
    return zeroCount

# Part 2

def numberOfZerosPassed(current, rotation):
    #if we go right
    if rotation >= 0:
        return ((current + rotation) - (current + rotation)%100) // 100
    #if we go left
    elif rotation < 0 :
        additional = 0
        if current != 0:
            additional = 1
        return additional + ((-(current + rotation)) - (-(current + rotation))%100) // 100

def solvingPart2():
    data = txtToList('entry1.txt')
    zeroCount = 0
    current = 50
    for move in data:
        rotation = int(move[1:])
        if move[0] == 'L':
            zeroCount += numberOfZerosPassed(current, -rotation)
            current -= rotation
        elif move[0] == 'R':
            zeroCount += numberOfZerosPassed(current, rotation)
            current += rotation
        current = current%100
    return zeroCount

# Main Execution

def main():
    resultPart1 = solvingPart1()
    print("Part 1 Result:", resultPart1)
    resultPart2 = solvingPart2()
    print("Part 2 Result:", resultPart2)

if __name__ == "__main__":
    main()
