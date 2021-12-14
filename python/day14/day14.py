import os
import queue
import time
from math import ceil, floor
from queue import LifoQueue
from collections import defaultdict


def main():
    # input
    print(os.getcwd())
    day = "14"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    part1, part2 = 0, 0

    rules = dict()
    template, _, *inRules = lines
    for r in inRules:
        a, b = r.split(" -> ")
        rules[a] = b

    pairCounter, elementCounter = defaultdict(int), defaultdict(int)

    # read pairs from template
    for a, b in zip(template, template[1:]):
        pairCounter[a+b] += 1
    for c in template:
        elementCounter[c] += 1
    steps = 40

    for i in range(steps):

        for (a, b), v in pairCounter.copy().items():
            newElement = rules[a+b]
            elementCounter[newElement] += v
            # create new pairs
            pairCounter[a + newElement] += v
            pairCounter[newElement + b] += v
            pairCounter[a+b] -= v

        if i == 9:
            part1 = max(elementCounter.values()) - min(elementCounter.values())
        if i == 39:
            part2 = max(elementCounter.values()) - min(elementCounter.values())
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
