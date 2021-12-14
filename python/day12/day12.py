import os
import queue
import time
from math import ceil, floor
from queue import LifoQueue
from collections import defaultdict
from collections import deque


def iterDFS(startNode, adj, part2=False):
    result = 0
    p = [[startNode], set(), False]
    paths = deque()
    paths.appendleft(p)
    while paths:
        nodeList, visitedSet, revisited = paths.popleft()
        currNode = nodeList[-1]
        if currNode == 'end':
            result += 1
        else:
            for v in adj[currNode]:
                if v.islower():
                    if not v in visitedSet:
                        paths.appendleft(
                            [nodeList + [v], visitedSet | {v}, revisited])
                    else:
                        if part2 and not revisited:
                            paths.appendleft(
                                [nodeList + [v], visitedSet, True])
                else:
                    paths.appendleft([nodeList + [v], visitedSet, revisited])
    return result


def main():
    # input
    print(os.getcwd())
    day = "12"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test3.txt'
    inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    # generate graph
    adj = defaultdict(list)
    for l in lines:
        u, v = l.split('-')
        if v != 'start':
            adj[u].append(v)
        if u != 'start':
            adj[v].append(u)

    part1 = iterDFS('start', adj)
    part2 = iterDFS('start', adj, True)
    duration = int((time.time() - start_time) * 1000000)
    header = "!" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
