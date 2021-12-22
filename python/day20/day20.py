import os

import time
from collections import defaultdict


class Grid:
    def __init__(self, rules=None) -> None:
        self.cells = defaultdict(int)
        self.xmin = 0
        self.xmax = 100
        self.ymin = 0
        self.ymax = 100
        self.rules = rules
        self.nb = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                   (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        self.infinite = 0
        self.padding = 1

    def getRule(self, x, y):
        idx = 0
        for n in self.nb:
            nx = x + n[0]
            ny = y + n[1]
            if (nx >= self.xmin and nx <= self.xmax and ny <= self.ymax and ny >= self.ymin):
                if self.cells[(nx, ny)] == 1:
                    idx = idx ^ 1
            else:
                idx = idx ^ self.infinite
            idx <<= 1

        idx >>= 1
        return idx

    def litPixels(self):
        return sum(1 if c == 1 else 0 for c in self.cells.values())

    def doStep(self):

        self.updateBorder()
        newCells = defaultdict(int)
        for y in range(self.ymin-1, self.ymax+1 + self.padding):
            for x in range(self.xmin-1, self.xmax+1 + self.padding):

                rule = self.getRule(x, y)

                if self.rules[rule] == 1:
                    newCells[(x, y)] = 1
        self.cells = newCells
        self.infinite = self.rules[self.infinite * (len(self.rules) - 1)]

    def updateBorder(self):
        self.xmin = min(self.cells, key=lambda x: x[0])[0]
        self.xmax = max(self.cells, key=lambda x: x[0])[0]
        self.ymin = min(self.cells, key=lambda x: x[1])[1]
        self.ymax = max(self.cells, key=lambda x: x[1])[1]
        

    def __str__(self) -> str:
        self.updateBorder()
        result = ""
        for y in range(self.ymin, self.ymax+1):
            for x in range(self.xmin, self.xmax+1):

                if self.cells[(x, y)] == 1:
                    result += "#"
                else:
                    result += '.'
            result += "\n"

        return str(result)


def main():
    # input
    print(os.getcwd())
    day = "20"
    year = "2021"
    inputFile = f'../inputs/day{day}_test.txt'
    # inputFile = f'../inputs/day{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    part1, part2 = 0, 0
    # parse rules
    rules = [1 if c == '#' else 0 for c in lines[0]]
    # parse grid
    grid20 = Grid(rules)
    for r in range(2, len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == '#':
                grid20.cells[(c, r-2)] = 1

    for i in range(50):
        if i == 2:
            part1 = grid20.litPixels()
        grid20.doStep()
    part2 = grid20.litPixels()

    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
