import os
import time
from math import ceil, floor
from queue import LifoQueue


def main():
    # input
    print(os.getcwd())
    day = "10"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()

    # part1 & part2
    illegalDict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    completeDict = {'(': 1, '[': 2, '{': 3, '<': 4}
    openPara = set(['(', '[', '<', '{'])
    openCloseDict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    completeScores = []

    for l in lines:
        lineIllegal = False
        stack = LifoQueue()
        for c in l:
            if c in openPara:
                stack.put(c)
            elif c != openCloseDict[stack.get()]:
                part1 += illegalDict[c]
                lineIllegal = True
        if not lineIllegal:
            score = 0
            while not stack.empty():
                score *= 5
                score += completeDict[stack.get()]
            completeScores.append(score)

    part2 = sorted(completeScores)[len(completeScores) // 2]

    # output

    duration = int((time.time() - start_time) * 1000000)
    header = "*" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
