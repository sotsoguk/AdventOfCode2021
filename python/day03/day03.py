import os
import time
import cmath
import bisect
import string


def main():
    # input
    print(os.getcwd())
    day = "03"
    year = "2021"
    inputFile = f'../inputs/day{day}.txt'
    start_time = time.time()
    print(inputFile)
    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # convert to ints
    input = [int(l, base=2) for l in lines]
    num_digits = len(lines[0])
    epsilon = [0] * num_digits
    for l in lines:
        for i, b in enumerate(l):
            if b == '1':
                epsilon[num_digits-i-1] += 1

    eps = "".join(["1" if c > len(lines)//2 else "0" for c in epsilon])
    gamma = eps.translate(eps.maketrans({'1': '0', '0': '1'}))

    part1 = int(eps[::-1], base=2) * int(gamma[::-1], base=2)

    duration = int((time.time() - start_time) * 1000000)
    # part2
    inp_sort = sorted(input)
    n = len(lines[0])
    to_check, lo_idx, hi_idx = (1 << (n-1)), 0, len(input)
    while (lo_idx < hi_idx-1):
        mid = (lo_idx+hi_idx) // 2
        b = bisect.bisect_left(inp_sort[lo_idx:hi_idx], to_check)
        if (b+lo_idx) <= mid:
            lo_idx += b
        else:
            hi_idx = lo_idx + b
            to_check -= (1 << (n-1))
        n -= 1
        to_check += (1 << (n-1))

    oxy = inp_sort[lo_idx]

    n = len(lines[0])
    to_check, lo_idx, hi_idx = (1 << (n-1)), 0, len(input)
    while (lo_idx < hi_idx-1):
        mid = (lo_idx+hi_idx) // 2
        b = bisect.bisect_left(inp_sort[lo_idx:hi_idx], to_check)

        if (b+lo_idx) <= mid:
            hi_idx = lo_idx+b
            to_check -= (1 << (n-1))
        else:
            lo_idx = lo_idx + b
        n -= 1
        to_check += (1 << (n-1))

    co2 = inp_sort[lo_idx]

    part2 = co2 * oxy
    print(
        f"AoC {year} - Day {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")


if __name__ == "__main__":
    main()
