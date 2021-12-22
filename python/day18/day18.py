import os
import queue
import time
import ast
from math import ceil, floor
from queue import LifoQueue
from collections import defaultdict

class Node:
    def __init__(self, parent = None, left = None, right=None, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None

        if left is not None:
            self.left = left
            self.left.parent = self
        if right is not None:
            self.right = right
            self.right.parent = self

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return '['+str(self.left)+','+str(self.right) + ']'

    def explode(self, node):
        l = node.left.value
        r = node.right.value
        node.left = None
        node.right = None
        node.value = 0
        self.addLeft(node,l)
        self.addRight(node,r)

    def addLeft(self,node,v):
        while True:
            if node == node.parent.right:
                self.addRightEnd(node.parent.left,v)
                return
            if node.parent is None:
                # nothing to do
                return
            else:
                node = node.parent

    def addRight(self,node,v):
        while True:
            if node == node.parent.left:
                self.addLeftEnd(node.parent.right,v)
                return
            if node.parent is None:
                # nothing to do
                return
            else:
                node = node.parent
    
    def addLeftEnd(self, node ,v):
        while node.left:
            node = node.left
            node.value += v

    def addRightEnd(self, node,v):
        while node.right:
            node = node.right
            node.value += v

    
    def explodeRecursive(self,node, level):
        if node.value is None:
            if level < 4:
                (x,nd) = self.explodeRecursive(node.left, level+1)
                if x:
                    return (x,nd)
                (x,nd) = self.explodeRecursive(node.right, level+1)
                if x:
                    return (x,nd)
                return (False, None)
            else:
                return (True,node)
        else:
            return (False, None)

    def check_for_explosions(self):
        return self.explodeRecursive(self,0)

    def check_for_split(self):
        return self.splitRecursive(self)

    def splitRecursive(self,node):
        if node.value is not None:
            if node.value >= 10:
                # need a split
                return (True,node)
            else:
                return (False, node)
        else:
            s,sn = self.splitRecursive(node.left)
            if s:
                return (s,sn)
            s,sn = self.splitRecursive(node.right)
            if s:
                return (s,sn)

            return (False,None)

    def split(self,node):
        node.left = Node(value=int(floor(node.value /2)),parent=node)              
        node.right = Node(value=int(ceil(node.value /2)),parent=node)
        node.value = None

    def reduce(self):
        while True:
            x,xn = self.check_for_explosions()
            if x:
                self.explode(xn)
                continue
            s, sn = self.check_for_split()
            if s:
                self.split(sn)
                continue
        return

    def magnitude(self):
        def mr(node):
            if node.value is not None:
                return node.value
            else:
                return 3*mr(node.left) + 2*mr(node.right)

        return mr(self)  
    
def parseRecursive(node,data):
    
    if isinstance(data,list):
        node.left = Node()
        parseRecursive(node.left,data[0])
        node.left.parent = node
        node.right = Node()
        parseRecursive(node.right,data[1])
        node.right.parent = node
    else:
        node.value = data

def parse(data):
    all_data = ast.literal_eval(data)
    node = Node()
    parseRecursive(node, all_data)
    return node

def sumAll(lines):
    snailfishsum = None
    for l in lines:
        node = parse(l)
        node.reduce()
        if snailfishsum is None:
            snailfishsum = node
        else:
            snailfishsum = Node(left=snailfishsum,right=node)
        snailfishsum.reduce()
    return snailfishsum.magnitude()


def main():
    # input
    print(os.getcwd())
    day = "18"
    year = "2021"
    # inputFile = f'../inputs/day{day}_test.txt'
    inputFile = f'../inputs/day{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    lines = [l.strip() for l in lines]
    
    part1 = sumAll(lines)
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
