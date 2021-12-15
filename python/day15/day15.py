import os
import queue
import time
from math import ceil, cos, floor
from queue import LifoQueue
from collections import defaultdict
from typing import Iterator, List, Tuple
import heapq
from PIL import Image, ImageDraw

class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: int):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def inBounds(pos, width, height):
    x, y = pos
    return 0 <= x < width and 0 <= y < height


def neighbors(pos, width, height):
    x, y = pos
    nb = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
    results = []
    for n in nb:
        if inBounds(n, width, height):
            results.append(n)
    return results


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    # return (abs(x1-x2) + abs(y1-y2))
    return 1
    # return 5*((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))


def solveCave(cave, part2=False):
    def cost(pos):
        x, y = pos
        if not part2:
            return cave[y][x]
        else:
            result = cave[y % tileHeight][x % tileWidth] + \
                x // tileWidth + y // tileHeight
            return result % 9 if result > 9 else result
    width, height = len(cave[0]), len(cave)
    tileWidth, tileHeight = width, height
    if part2:
        width *= 5
        height *= 5

    q = PriorityQueue()
    q.put((0, 0), 0)
    pathRisk = dict()
    pathRisk[(0, 0)] = 0
    goal = (width-1, height-1)

    while not q.empty():
        current = q.get()
        if current == goal:
            break
        for nn in neighbors(current, width, height):
            new_cost = pathRisk[current] + cost(nn)
            if nn not in pathRisk or new_cost < pathRisk[nn]:
                pathRisk[nn] = new_cost
                prio = new_cost + heuristic(goal,nn)# width-1-nn[0]+height-1-nn[1] #heuristic(goal, nn)
                q.put(nn, prio)
    return(pathRisk[goal])

def solveCaveWithPath(cave, part2=False):
    def cost(pos):
        x, y = pos
        if not part2:
            return cave[y][x]
        else:
            result = cave[y % tileHeight][x % tileWidth] + \
                x // tileWidth + y // tileHeight
            return result % 9 if result > 9 else result
    width, height = len(cave[0]), len(cave)
    tileWidth, tileHeight = width, height
    if part2:
        width *= 5
        height *= 5

    q = PriorityQueue()
    q.put((0, 0), 0)
    pathRisk = dict()
    pathRisk[(0, 0)] = 0
    goal = (width-1, height-1)
    cameFrom = dict()
    cameFrom[(0,0)] = None
    while not q.empty():
        current = q.get()
        if current == goal:
            break
        for nn in neighbors(current, width, height):
            new_cost = pathRisk[current] + cost(nn)
            if nn not in pathRisk or new_cost < pathRisk[nn]:
                pathRisk[nn] = new_cost
                prio = new_cost + heuristic(goal, nn)
                q.put(nn, prio)
                cameFrom[nn] = current
    # create path
    path = []
    nnn = goal
    while nnn:
        path.append(nnn)
        nnn = cameFrom[nnn]
    path.reverse()
    return(pathRisk[goal],path)
def createImage(cave, path, scaleFactor):
    w, h = len(cave[0]), len(cave)

    img = Image.new('RGB', (w*scaleFactor,h*scaleFactor),color=(100,100,100))
    colorPalete = {1:"#2E4272",2:"#2E4272",3:"#7887AB",4:"#7887AB",5:"#4F628E",6:"#4F628E",7:"#162955",8:"#162955",9:"#061539"}
    d = ImageDraw.Draw(img)
    # d.text((10,10),"5",fill=(255,255,0))
    for r in range(h):
        for c in range(w):
            x0 = c*scaleFactor
            y0 = r * scaleFactor
            x1 = (c+1)*scaleFactor
            y1 = (r+1) * scaleFactor
            rcol = (255//10)*(10-cave[r][c])
            # print(r,c," -> ",x0,y0,x1,y1,rcol)
            d.rectangle([(x0,y0),(x1,y1)],fill=(10,10,rcol))
    img.save("img00000.jpg")
    for i,p in enumerate(path):
        c,r = p
        x0 = c*scaleFactor
        y0 = r * scaleFactor
        x1 = (c+1)*scaleFactor
        y1 = (r+1) * scaleFactor
        fcol = (128,128,128)
        # print(r,c," -> ",x0,y0,x1,y1,rcol)
        d.rectangle([(x0,y0),(x1,y1)],fill="#F8D210")
        img.save(f'img{i+1:05d}.jpg')
def main():
    # input
    print(os.getcwd())
    day = "15"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    part1, part2 = 0, 0

    cave = []
    for l in lines:
        cave.append(list(map(int, l)))

    part1 = solveCave(cave)
    part2 = solveCave(cave,True)
    
    # part1, path1 = solveCaveWithPath(cave)
    # print(path1)
    # createImage(cave,path1, 10)
    # part2 = solveCave(cave, True)
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
