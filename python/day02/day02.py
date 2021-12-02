import os
import time
import cmath


def main():
    # input
    print(os.getcwd())
    day = "02"
    year = "2021"
    inputFile = f'../inputs/day{day}.txt'
    print(inputFile)
    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # convert commands to complex numbers
    commands = {'forward': 1+0j, 'down': 0+1j, 'up': 0-1j}

    start_time = time.time()
    # parse input

    def conv(line): return (
        commands[line.split(" ")[0]], int(line.split(" ")[1]))
    instructions = [conv(l) for l in lines]

    # part1
    final_position = sum(c[0] * c[1] for c in instructions)
    part1 = int((final_position.real * final_position.imag))

    # part2
    aim = 0
    final_position_2 = 0+0j
    for i in instructions:
        if i[0] == 1+0j:
            final_position_2 += i[0]*i[1]
            final_position_2 += (0+1j)*aim*i[1]
        else:
            aim += (i[0]*i[1]).imag

    part2 = int(final_position_2.real * final_position_2.imag)
    duration = int((time.time() - start_time) * 1000000)

    print(
        f"AoC {year} - Day {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")


if __name__ == "__main__":
    main()
