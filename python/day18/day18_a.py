

import ast
import copy
import math
import sys

class SnailfishNode:
    def __init__(self, parent=None, left=None, right=None, value=None):
        self.value = value
        self.left = None
        if left is not None:
            self.left = left
            self.left.parent = self
        self.right = None
        if right is not None:
            self.right = right
            self.right.parent = self
        self.parent = parent

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return '[' + str(self.left) + ',' + str(self.right) + ']'

    def explode_rec(self, sfn, level):
        if sfn.value is None:
            if level < 4:
                (exploded, node) = self.explode_rec(sfn.left, level+1)
                if exploded:
                    return (exploded, node)
                (exploded, node) = self.explode_rec(sfn.right, level+1)
                if exploded:
                    return (exploded, node)
                return (False, None)
            else:
                return (True, sfn)
        else:
            return (False, None)

    def find_explode_if_needed(self):
        return self.explode_rec(self, 0)

    def add_to_left(self, node, number):
        while True:
            if node.parent is None:
                return
            if node == node.parent.right:
                self.add_rightmost(node.parent.left, number)
                return
            else:
                node = node.parent

    def add_rightmost(self, node, number):
        while node.right:
            node = node.right
        node.value += number

    def add_to_right(self, node, number):
        while True:
            if node.parent is None:
                return
            if node == node.parent.left:
                self.add_leftmost(node.parent.right, number)
                return
            else:
                node = node.parent

    def add_leftmost(self, node, number):
        while node.left:
            node = node.left
        node.value += number

    def explode(self, node):
        left = node.left.value
        right = node.right.value
        node.left = None
        node.right = None
        node.value = 0
        self.add_to_left(node, left)
        self.add_to_right(node, right)

    def split_rec(self, node):
        if node.value is not None:
            if node.value >= 10:
                return (True, node)
            else:
                return (False, node)
        else:
            split, split_node = self.split_rec(node.left)
            if split:
                return (split, split_node)
            split, split_node = self.split_rec(node.right)
            if split:
                return (split, split_node)
            return (False, None)

    def find_split_if_needed(self):
        return self.split_rec(self)

    def split(self, node):
        node.left = SnailfishNode(value=int(math.floor(node.value / 2)), parent=node)
        node.right = SnailfishNode(value=int(math.ceil(node.value / 2)), parent=node)
        node.value = None

    def reduce(self):
        while True:
            exploded, node = self.find_explode_if_needed()
            if exploded:
                self.explode(node)
                continue
            split, node = self.find_split_if_needed()
            if split:
                self.split(node)
                continue
            return

    def magnitude(self):
       def magnitude_rec(node):
           if node.value is not None:
               return node.value
           else:
               return magnitude_rec(node.left) * 3 + magnitude_rec(node.right) * 2

       return magnitude_rec(self)

def parse_rec(sfn, data):
    if isinstance(data, list):
        sfn.left = SnailfishNode()
        parse_rec(sfn.left, data[0])
        sfn.left.parent = sfn
        sfn.right = SnailfishNode()
        parse_rec(sfn.right, data[1])
        sfn.right.parent = sfn
    else:
        sfn.value = data

def parse_snailfish(data):
    sfn_data = ast.literal_eval(data)
    sfn = SnailfishNode()
    parse_rec(sfn, sfn_data)
    return sfn

def sum_all(lines):
    sfn_sum = None
    for line in lines:
        sfn = parse_snailfish(line)
        sfn.reduce()
        if sfn_sum is None:
            sfn_sum = sfn
        else:
            sfn_sum = SnailfishNode(left=sfn_sum, right=sfn)
        sfn_sum.reduce()
    return sfn_sum.magnitude()

def sum_two(lines):
    fish = []
    for line in lines:
        sfn = parse_snailfish(line)
        sfn.reduce()
        fish.append(sfn)

    max_magnitude = 0
    for i in range(len(fish)):
        for j in range(len(fish)):
            if i != j:
                sfn_sum = SnailfishNode(left=copy.deepcopy(fish[i]), right=copy.deepcopy(fish[j]))
                sfn_sum.reduce()
                magnitude = sfn_sum.magnitude()
                if magnitude > max_magnitude:
                    max_magnitude = magnitude
    return max_magnitude

def main():
    #lines = [line.strip() for line in sys.stdin.readlines()]
    day = 18
    inputFile = f'../inputs/day{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    # Part1
    print(sum_all(lines))
    # Part2
    print(sum_two(lines))

if __name__ == "__main__":
    main()