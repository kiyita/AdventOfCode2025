"""
Advent of Code Day 2 Solution
Author: Lucie
Date: 2025-12-02
Python 3
"""

# Part 1

def txtToList(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    result = [item.strip() for item in content.split(",") if item.strip()]
    for i in range(len(result)):
        result[i] = (int(result[i].split("-")[0]), int(result[i].split("-")[1]))
    return result

def solvingPart1():
    datas = txtToList("entry2.txt")
    count = 0
    for data in datas:
        for i in range(data[0], data[1] + 1):
            if str(i)[0:len(str(i))//2] == str(i)[len(str(i))//2:len(str(i)) + 1]:
                count += i
    return count

# Part 2

def solvingPart2():
    datas = txtToList("entry2.txt")
    count = 0
    for data in datas:
        for id in range(data[0], data[1] + 1):
            for j in range(1, len(str(id))//2 + 1):
                if (str(id)[0:j] * (len(str(id))//j)) == str(id):
                    count += id
                    break
    return count

# Main Execution

def main():
    part1_result = solvingPart1()
    print("Part 1 Result:", part1_result)
    
    part2_result = solvingPart2()
    print("Part 2 Result:", part2_result)

if __name__ == "__main__":
    main()
