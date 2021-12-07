import os
import time
from math import ceil, floor


def main():
    # input
    print(os.getcwd())
    day = "07"
    year = "2021"
    inputFile = f'../inputs/day{day}_test.txt'
    # inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    # parse input
    inp = list(map(int, lines[0].split(',')))

    # part1
    inp.sort()
    median = inp[len(inp) // 2]
    part1 = sum([abs(median-crab) for crab in inp])

    # part2
    avg1 = int(floor(sum(inp) / len(inp)))
    avg2 = int(ceil(sum(inp) / len(inp)))
    part2 = min(sum([abs(i-avg1)*(abs(i-avg1)+1)//2 for i in inp]),
                sum([abs(i-avg2)*(abs(i-avg2)+1)//2 for i in inp]))
    # output

    duration = int((time.time() - start_time) * 1000000)
    header = "*" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
