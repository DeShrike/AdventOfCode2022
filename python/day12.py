from aoc import Aoc
import itertools
import math
import re
import sys

# Day 12
# https://adventofcode.com/2022

class Dykstra:
    def __init__(self, matrix):
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.start = None
        self.end = None
        self.graph = self.prepare_graph(matrix)

    class Node:
        def __init__(self, x, y, weight=0):
            self.x = x
            self.y = y
            self.weight = weight
            self.neighbors = []
            self.is_goal = False
            self.is_start = False
            self.dist = 1_000_000_000
            self.prev = None

        def __repr__(self):
            s = f"Node({self.x}, {self.y}, {self.weight})\n"
            for n in self.neighbors:
                s += f"  N: {n.x}, {n.y}\n"
            return s

    def prepare_graph(self, mat):
        graph = {}
        for y, line in enumerate(mat):
            for x, weight in enumerate(line):
                if weight == "S":
                    node = self.Node(x, y, weight=1)
                    self.start = node
                    node.is_start = True
                elif weight == "E":
                    node = self.Node(x, y, weight=26)
                    node.is_goal = True
                    self.end = node
                else:
                    node = self.Node(x, y, weight=ord(weight) - 96)

                graph[(x, y)] = node

        for k, node in graph.items():
            node.neighbors = list(self.neighbours(graph, node))

        return graph

    def equal(self, current, end):
        return current.x == end.x and current.y == end.y

    def neighbours(self, graph, current):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y = current.x, current.y
        for dir in dirs:
            if x + dir[0] >= 0 and x + dir[0] < self.width and y + dir[1] >= 0 and y + dir[1] < self.height:
                this = graph[(x + dir[0], y + dir[1])]
                if this.weight <= current.weight + 1:
                    yield this

    def smallest(self, lijst):
        d = 1_000_000
        i = None
        for node in lijst:
            if node.dist < d:
                d = node.dist
                i = node
        return i

    def run(self):
        graph = self.graph
        start = self.start
        end = self.end
        Q = [v for key, v in graph.items()]
        start.dist = 0

        while len(Q) > 0:
            u = self.smallest(Q)
            Q.remove(u)

            if self.equal(u, end):
                p = []
                while u.prev is not None:
                    p.append(u.prev)
                    u = u.prev
                return p

            for v in u.neighbors:
                if v not in Q:
                    continue
                alt = u.dist + u.weight
                if alt < v.dist:
                    v.dist = alt
                    v.prev = u

        return None


class Day12Solution(Aoc):

    def Run(self):
        self.StartDay(12, "Hill Climbing Algorithm")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(12)

        goal = self.TestDataA()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

    def TestDataA(self):
        self.inputdata.clear()
        testdata = \
        """
        Sabqponm
        abcryxxl
        accszExk
        acctuvwj
        abdefghi
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 31

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 29

    def PartA(self):
        self.StartPartA()

        d = Dykstra(self.inputdata)
        
        print(f" Width: {d.width}")
        print(f"Height: {d.height}")

        p = d.run()
        answer = len(p)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day12Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

