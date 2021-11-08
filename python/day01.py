import os
from itertools import accumulate

import time

def main():
    # input
    print(os.getcwd())
    day = "01"
    inputFile = f'../inputs/day{day}.txt'
    print(inputFile)
    part1, part2 = 0,0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    
    start_time = time.time()
    
    # part1
    nP = [1 if c=="(" else -1 for c in lines[0]]
    aP = list(accumulate(nP))
    part1 = aP[-1]
    part2 = aP.index(-1)+1
    duration = int((time.time() - start_time) * 1000000)

    print(f"AoC 2015 - Day {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")

   
if __name__ == "__main__":
    main()