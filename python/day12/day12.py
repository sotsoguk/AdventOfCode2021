import os
import queue
import time
from math import ceil, floor
from queue import LifoQueue
from collections import defaultdict


def recDFS2(node,visited,adj,double_visit):
    if node == 'end':
        return 1
    # print(node,visited)
    # if node == 'start':
    #     return 0
    tmp = 0
    print(node,visited,double_visit,twice)
    if double_visit == True:
        if node.islower():
            visited.add(node)
        for v in adj[node]:
            if v == 'start':
                continue
            if v not in visited:
                tmp +=recDFS2(v,visited.copy(),adj,True,twice)
    else:
        if node == 'start':
            visited.add('start')
            for v in adj[node]:
                
                tmp +=recDFS2(v,visited.copy(),adj,False,[])
        else:
            if node.islower():
                visited2 = visited.copy()
                visited2.add(node)
            
            for v in adj[node]:
                if v == 'start':
                    continue
                if v not in visited:
                    if v == 'start':
                        continue
                
                    tmp += recDFS2(v,visited.copy(),adj,False,)
                    tmp += recDFS2(v,visited2.copy(),adj,True)
    return tmp
def recDFS(node,visited,adj):
    if node == 'end':
        return 1
    # print(node,visited)
    # if node == 'start':
    #     return 0
    if node.islower():
        visited.add(node)
    tmp = 0
    for v in adj[node]:
        if v == 'start':
            continue
        if v not in visited:
            tmp +=recDFS(v,visited.copy(),adj)
    return tmp
def main():
    # input
    print(os.getcwd())
    day = "12"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test2.txt'
    inputFile = f'../inputs/day{day}.txt'

    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    start_time = time.time()
    # generate graph
    adj = defaultdict(list)
    for l in lines:
        u,v = l.split('-')
        if v != 'start':
            adj[u].append(v)
        if u != 'start':
            adj[v].append(u)

    print(adj)
    # visited = set()
    # visited.add('start')
    # part1 = recDFS('start',visited,adj)
    # part2 = recDFS2('start',visited,adj, False,[])
    # part1
    p = [['start'],set(),False]
    paths = []
    paths.append(p)
    while paths:
        nodelist, visset, _ = paths.pop(0)
        #print(nodelist,visset)
        currNode = nodelist[-1]
        if currNode == 'end':
            part1 +=1
        else:
            for v in adj[currNode]:
                if v.islower():
                    if not v in visset:
                        paths.append([nodelist + [v],visset | {v},False])
                else:
                    paths.append([nodelist + [v],visset,False])

    # part2 
    p = [['start'],set(),False]
    paths = []
    paths.append(p)
    while paths:
        nodelist, visset, revisited = paths.pop(0)
        #print(nodelist,visset)
        currNode = nodelist[-1]
        if currNode == 'end':
            part2 +=1
        else:
            for v in adj[currNode]:
                if v.islower():
                    if not v in visset:
                        paths.append([nodelist + [v],visset | {v},revisited])
                    else:
                        if not revisited:
                            paths.append([nodelist + [v],visset, True])
                else:
                    paths.append([nodelist + [v],visset,revisited])
    duration = int((time.time() - start_time) * 1000000)
    header = "!" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
