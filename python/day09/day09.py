import os
import time
import numpy as np
from collections import deque


def getN(x, y, rows, cols):
    n = []
    if x > 0:
        n.append((y, x-1))
    if x < cols-1:
        n.append((y, x+1))
    if y > 0:
        n.append((y-1, x))
    if y < rows-1:
        n.append((y+1, x))
    return n





def getBasin(hmap, x, y):
    rows, cols = hmap.shape
    q = deque()
    basin = []
    visited = set()
    q.append((y, x))
    while q:
        currPos = q.popleft()
        if currPos in visited:
            continue
        visited.add(currPos)
        basin.append(currPos)
        currVal = hmap[currPos]
        
        ns = getN(currPos[1],currPos[0],rows,cols)
        for n in ns:
            if hmap[n] > currVal and hmap[n] < 9:
                q.append(n)

    return basin


def main():
    # input
    print(os.getcwd())
    day = "09"
    year = "2021"
    inputFile = f'../inputs/day{day}.txt'
    # inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    # parse input
    input = [list(map(int, l)) for l in lines]
    heightMap = np.array(input)

    # part1
    rows, cols = heightMap.shape
    minPos = []
    for y in range(rows):
        for x in range(cols):
            v = heightMap[y, x]
            neighbors = [heightMap[p] for p in getN(x, y, rows, cols)]
            if all(n > v for n in neighbors):
                minPos.append((y, x))

    part1 = sum([heightMap[p]+1 for p in minPos])

    # part2

    basins = sorted(map(lambda x: len(x), [getBasin(heightMap, pos[1], pos[0])
                                           for pos in minPos]), reverse=True)

    part2 = np.prod(basins[:3])
    duration = int((time.time() - start_time) * 1000000)
    header = "*" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
