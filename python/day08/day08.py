import os
import time
from math import ceil, floor
from collections import defaultdict, Counter
# 1: 2
# 4:4
# 7:3
# 8:7


def getNumber(wires):
    nums = {119: 0, 18: 1, 93: 2, 91: 3, 58: 4,
            107: 5, 111: 6, 82: 7, 127: 8, 123: 9}
    return nums[wires]


def decode(inp, out):
    sbl = defaultdict(list)
    cnt = defaultdict(int)

    for i in inp:
        sbl[len(i)].append(set(i))

    for i in inp:
        for j in i:
            cnt[j] += 1

    table = dict(); dg = []; ac = []
    for k, v in cnt.items():
        if v == 4:
            table[k] = 'e'
        elif v == 6:
            table[k] = 'b'
        elif v == 9:
            table[k] = 'f'
        elif v == 7:
            dg.append(k)
        else:
            ac.append(k)
    bd = (sbl[4][0].difference(sbl[2][0]))
    d = bd.intersection(set(dg))
    dv = d.pop()
    dg.remove(dv)
    g = dg[0]
    table[g] = 'g'
    table[dv] = 'd'

    # detect a and c
    ta = sbl[3][0].difference(sbl[2][0]).pop()
    table[ta] = 'a'
    ac.remove(ta)
    table[ac[0]] = 'c'
    wireToNum = {'a': 64, 'b': 32, 'c': 16, 'd': 8, 'e': 4, 'f': 2, 'g': 1}
    nums = {119: 0, 18: 1, 93: 2, 91: 3, 58: 4,
            107: 5, 111: 6, 82: 7, 127: 8, 123: 9}
    result = []
    for o in out:
        otr = o.translate(o.maketrans(table))
        temp = 0
        for c in otr:
            temp += wireToNum[c]
        result.append(str(nums[temp]))

    return int("".join(result))


def main():
    # input
    print(os.getcwd())
    day = "08"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    # parse input

    inp = []
    out = []
    for l in lines:
        inp.append(l.split()[:10])
        out.append(l.split()[11:])

    p1 = set([2, 3, 4, 7])
    for i in out:
        part1 += sum(1 if len(d) in p1 else 0 for d in i)
    # part 2

    for i in range(len(inp)):
        part2 += decode(inp[i], out[i])

    duration = int((time.time() - start_time) * 1000000)
    header = "*" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
