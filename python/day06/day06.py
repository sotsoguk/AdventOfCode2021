import os
import time
import re
from collections import defaultdict,Counter


def main():
    # input
    print(os.getcwd())
    day = "06"
    year = "2021"
    inputFile = f'../inputs/day{day}.txt'
    # inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    # parse input
    inp = list(map(int,lines[0].split(',')))
  
    fish = defaultdict(int,Counter(inp))
  

    
    days_1 = 80
    days = 256
    for i in range(days):
        if i == days_1:
            part1 = sum(fish.values())
        nextfish = defaultdict(int)
        for d in range(9):
            if d == 0:
                nextfish[8] = fish[0]
                nextfish[6] = fish[0]
            else:
                nextfish[d-1] += fish[d]
        fish = nextfish
    
   
    part2 = sum(fish.values())
    duration = int((time.time() - start_time) * 1000000)
    header = "*" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
