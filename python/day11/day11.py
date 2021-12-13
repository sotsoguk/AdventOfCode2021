import os
import queue
import time
from math import ceil, floor
from queue import LifoQueue


def main():
    # input
    print(os.getcwd())
    day = "11"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    grid = []
    for l in lines:
        # print(l)
        # print(l.split())
        grid.append(list(map(int,l)))

    # part1 & part2
    rows, cols = len(lines), len(lines[0])
    print(rows,cols)
    ns = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
    steps = 1000
    for i in range(steps):
        ## check part2
        if all(sum(r)==0 for r in grid):
            part2 = i
            break
        q = []
        for r in range(rows):
            for c in range(cols):
                # print(r,c,grid[r][c])
                grid[r][c] += 1
                if grid[r][c]==10:
                    q.append((r,c))
        # flashes
        while len(q) > 0:
            r,c = q.pop(0)
            grid[r][c] = 0
            part1 += 1
            # determine neighbors
            for dx,dy in ns:
                nc = c + dx
                nr = r + dy
                if nc in range(cols) and nr in range(rows):
                    if grid[nr][nc] >0 and grid[nr][nc] < 10:
                        grid[nr][nc] += 1
                        if grid[nr][nc] == 10:
                            q.append((nr,nc))
    # output

    duration = int((time.time() - start_time) * 1000000)
    header = "!" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
