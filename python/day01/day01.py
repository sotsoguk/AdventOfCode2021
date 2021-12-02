import os
import time


def main():
    # input
    print(os.getcwd())
    day = "01"
    year = "2021"
    inputFile = f'../inputs/day{day}.txt'
    print(inputFile)
    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()

    input = list(map(int, lines))

    start_time = time.time()

    # part1 & 2
    part1 = sum(b > a for (a, b) in zip(input, input[1:]))
    part2 = sum(b > a for (a, b) in zip(input, input[3:]))

    duration = int((time.time() - start_time) * 1000000)

    print(
        f"AoC {year} - Day {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")


if __name__ == "__main__":
    main()
