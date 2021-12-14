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
    maxX, maxY = max(grid,key = lambda x:x[0])[0],max(grid,key = lambda x:x[1])[1]
    printGrid = []
    for r in range(maxY+1):
        printGrid.append([0]*(maxX+1))
    for d in grid:
        printGrid[d[1]][d[0]] = 1
    for r in range(len(printGrid)):
        l = u''
        for c in range(len(printGrid[0])):
            if printGrid[r][c] == 0:
                l+=u' '
            else:
                l+=u'#'
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
    instructions=[]
    
    for l in lines[:lines.index("")]:
        a,b = list(map(int,l.split(',')))
        dots.append((a,b))
    
    for l in lines[lines.index("")+1:]:
        tmp = l.split()[2]
        instructions.append((tmp[0],int(tmp[2:])))
   
    for c,i in enumerate(instructions):
        if i[0] == 'x':
            dots = foldX(dots,i[1])
        else:
            dots = foldY(dots,i[1])
        
        if c == 0:
            part1 = len(set(dots))
        
    printGrid(dots)
    print(dots)
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")
    

if __name__ == "__main__":
    main()
