from aoc import Aoc
from canvas import Canvas
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

        def has_climbing_neigbors(self) -> bool:
            return any([n for n in self.neighbors if n.weight == self.weight + 1])

        def __repr__(self):
            s = f"Node({self.x}, {self.y}, {self.weight})\n"
            for n in self.neighbors:
                s += f"  N: {n.x}, {n.y}\n"
            return s

    def reset(self):
        for k, node in self.graph.items():
            node.dist = 1_000_000_000
            node.prev = None

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
        if len(lijst) == 0:
            return None
        lijst.sort(key=lambda n: n.dist)

        return lijst[0]

    def run(self):
        graph = self.graph
        start = self.start
        end = self.end
        Q = [v for key, v in graph.items()]
        start.dist = 0

        while len(Q) > 0:
            u = self.smallest([ n for n in Q if n.dist != 1_000_000_000 ])
            if u is None:
                return None
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
        self.TestDataA()
        return 29

    def addsquare(self, canvas: Canvas, x: int, y: int, mult: int, color):
        x = x * mult
        y = y * mult
        for xx in range(mult):
            for yy in range(mult):
                canvas.set_pixel(x + xx, y + yy, color)

    def PartA(self):
        self.StartPartA()

        d = Dykstra(self.inputdata)
        
        print(f" Width: {d.width}")
        print(f"Height: {d.height}")

        p = d.run()

        mult = 2
        canvas = Canvas(d.width * mult, d.height * mult)
        for k, node in d.graph.items():
            color = (255 // 26) * node.weight
            self.addsquare(canvas, k[0], k[1], mult, (color, color, color))

        for pos in p:
            node = pos
            color = (255 // 26) * node.weight
            self.addsquare(canvas, node.x, node.y, mult, (color, 0, 0))

        print("Saving")
        canvas.save_PNG("day12.png")

        answer = len(p)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = None
        d = Dykstra(self.inputdata)
        starts = [k for k,v in d.graph.items() if v.weight == 1 and v.has_climbing_neigbors()]
        print(len(starts))

        lengths = []

        for ix, start in enumerate(starts):
            print(f"{ix}/{len(starts)} -> {start}")
            d.reset()
            d.start = d.graph[start]
            p = d.run()
            if p is None:
                print("No path")
                continue
            print(len(p))
            lengths.append(len(p))

        answer = min(lengths)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day12Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

