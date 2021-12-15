import os
import queue
import time
from math import ceil, cos, floor
from queue import LifoQueue
from collections import defaultdict
from typing import Iterator, List, Tuple
import heapq


class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: int):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def inBounds(pos, width, height):
    x, y = pos
    return 0 <= x < width and 0 <= y < height


def neighbors(pos, width, height):
    x, y = pos
    nb = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
    results = []
    for n in nb:
        if inBounds(n, width, height):
            results.append(n)
    return results


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2) + abs(y1-y2)


def solveCave(cave, part2=False):
    def cost(pos):
        x, y = pos
        if not part2:
            return cave[y][x]
        else:
            result = cave[y % tileHeight][x % tileWidth] + \
                x // tileWidth + y // tileHeight
            return result % 9 if result > 9 else result
    width, height = len(cave[0]), len(cave)
    tileWidth, tileHeight = width, height
    if part2:
        width *= 5
        height *= 5

    q = PriorityQueue()
    q.put((0, 0), 0)
    pathRisk = dict()
    pathRisk[(0, 0)] = 0
    goal = (width-1, height-1)

    while not q.empty():
        current = q.get()
        if current == goal:
            break
        for nn in neighbors(current, width, height):
            new_cost = pathRisk[current] + cost(nn)
            if nn not in pathRisk or new_cost < pathRisk[nn]:
                pathRisk[nn] = new_cost
                prio = new_cost + heuristic(goal, nn)
                q.put(nn, prio)
    return(pathRisk[goal])


def main():
    # input
    print(os.getcwd())
    day = "15"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    part1, part2 = 0, 0

    cave = []
    for l in lines:
        cave.append(list(map(int, l)))

    part1 = solveCave(cave)
    part2 = solveCave(cave, True)
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
