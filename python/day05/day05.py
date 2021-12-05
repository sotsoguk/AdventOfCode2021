import os
import time
import re
from collections import defaultdict


def main():
    # input
    print(os.getcwd())
    day = "05"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt
    inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    # parse input
    input = [list(map(int, re.findall('\d+', l))) for l in lines]
    grid = defaultdict(int)
    diagonals = []

    # part1

    for l in input:
        # horizontal
        x1, y1, x2, y2 = l
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid[(i, y1)] += 1
        # vertical
        elif x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                grid[(x1, i)] += 1
        else:
            diagonals.append(l)

    part1 = sum([1 if v > 1 else 0 for v in grid.values()])

    # part 2

    for l in diagonals:
        x1, y1, x2, y2 = l
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        for i in range(abs(x2-x1)+1):
            grid[(x1+i*dx, y1+i*dy)] += 1

    part2 = sum([1 if v > 1 else 0 for v in grid.values()])

    # output

    duration = int((time.time() - start_time) * 1000000)
    header = "*" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
