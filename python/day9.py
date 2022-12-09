from aoc import Aoc
import itertools
import math
import re
import sys

# Day 9
# https://adventofcode.com/2022

class Day9Solution(Aoc):

    def Run(self):
        self.StartDay(9, "Rope Bridge")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(9)

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
        R 4
        U 4
        L 3
        D 1
        R 4
        D 1
        L 5
        R 2
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 13

    def TestDataB(self):
        self.inputdata.clear()
        testdata = \
        """
        R 5
        U 8
        L 8
        D 3
        R 17
        D 10
        L 25
        U 20
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 36

    def head_9by9(self):
        yield (self.hx-1, self.hy-1)
        yield (self.hx  , self.hy-1)
        yield (self.hx+1, self.hy-1)
        yield (self.hx-1, self.hy)
        yield (self.hx  , self.hy)
        yield (self.hx+1, self.hy)
        yield (self.hx-1, self.hy+1)
        yield (self.hx  , self.hy+1)
        yield (self.hx+1, self.hy+1)

    def sq9by9(self, x: int, y: int):
        yield (x - 1, y - 1)
        yield (x    , y - 1)
        yield (x + 1, y - 1)
        yield (x - 1, y)
        yield (x    , y)
        yield (x + 1, y)
        yield (x - 1, y + 1)
        yield (x    , y + 1)
        yield (x + 1, y + 1)

    def istouching(self) -> bool:
        return (self.tx, self.ty) in list(self.head_9by9())

    def is_touching(self, x1:int, y1:int, x2:int, y2:int) -> bool:
        return (x1, y1) in list(self.sq9by9(x2, y2))

    def step(self, direction: str):
        moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        self.hx += moves[direction][0]
        self.hy += moves[direction][1]
        if not self.istouching():
            if self.tx == self.hx or self.ty == self.hy:    # orthogonal
                self.tx += moves[direction][0]
                self.ty += moves[direction][1]
            else:                                           # diagonal
                if self.tx < self.hx:
                    self.tx += moves["R"][0]
                    self.ty += moves["R"][1]
                else:
                    self.tx += moves["L"][0]
                    self.ty += moves["L"][1]

                if self.ty < self.hy:
                    self.tx += moves["D"][0]
                    self.ty += moves["D"][1]
                else:
                    self.tx += moves["U"][0]
                    self.ty += moves["U"][1]

    def PartA(self):
        self.StartPartA()

        positions = set()
        self.hx = self.hy = self.tx = self.ty = 0

        for line in self.inputdata:
            direction = line.split(" ")[0]
            steps = int(line.split(" ")[1])
            for _ in range(steps):
                self.step(direction)
                positions.add((self.tx, self.ty))

        answer = len(positions)

        self.ShowAnswer(answer)

    def step_rope(self, direction:str):
        moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        self.rope[0][0] += moves[direction][0]
        self.rope[0][1] += moves[direction][1]
        for h in range(self.rope_length - 1):
            t = h + 1
            if not self.is_touching(*self.rope[h], *self.rope[t]):
                pass

    def PartB(self):
        self.StartPartB()

        positions = set()
        self.rope_length = 10
        self.rope = [[0, 0] for _ in range(self.rope_length)]

        for line in self.inputdata:
            direction = line.split(" ")[0]
            steps = int(line.split(" ")[1])
            for _ in range(steps):
                self.step_rope(direction)
                positions.add((self.rope[-1][0], self.rope[-1][1]))


        answer = len(positions)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day9Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

