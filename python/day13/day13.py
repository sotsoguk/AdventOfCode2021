import os
import queue
import time
from math import ceil, floor
from queue import LifoQueue
from collections import defaultdict

def foldX(dots,axis):
    newDots = []
    for d in dots:
        if d[0]>axis:
            newDots.append((2*axis-d[0],d[1]))
        else:
            newDots.append(d)
    return newDots

def foldY(dots,axis):
    newDots = []
    for d in dots:
        if d[1]>axis:
            newDots.append((d[0],2*axis-d[1]))
        else:
            newDots.append(d)
    return newDots
def printGrid(grid):
    minX = 1000
    minY = 1000
    maxX = 0
    maxY = 0
    for d in grid:
        minX = min(minX,d[0])
        minY = min(minY,d[1])
        maxX = max(maxX,d[0])
        maxY = max(maxY,d[1])
    print(minX,minY,maxX,maxY)
    pgrid = []
    for r in range(maxY+1):
        pgrid.append([0]*(maxX+1))
    print(pgrid)
    for d in grid:
        # print(d[1],d[0])
        pgrid[d[1]][d[0]] = 1
    print(pgrid)
    for r in range(len(pgrid)):
        l = u''
        for c in range(len(pgrid[0])):
            if pgrid[r][c] == 0:
                l+=u' '
            else:
                l+=u'\u2588'
        print(l.encode('utf8'))
def main():
    # input
    print(os.getcwd())
    day = "13"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    part1, part2 = 0,0
    dots = []
    lnr = 0
    instructions=[]
    while True:
        if lines[lnr] != "":
            a,b = lines[lnr].split(',')
            dots.append((int(a),int(b)))
            lnr += 1
        else:
            lnr +=1
            break
    for i in range(lnr,len(lines)):
        tmp = lines[i].split()[2]
        instructions.append((tmp[0],int(tmp[2:])))
    
    print(dots)
    for i in instructions:
        if i[0] == 'x':
            dots = foldX(dots,i[1])
        else:
            dots = foldY(dots,i[1])
        print("!!!! ",i)
        print(len(set(dots)))
        # print(dots)
    printGrid(dots)
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")
    pinrt

if __name__ == "__main__":
    main()
