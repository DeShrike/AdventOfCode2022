from aoc import Aoc
from canvas import Canvas
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

    def head_9by9(self):
        yield from self.sq9by9(self.hx, self.hy)

    def istouching(self) -> bool:
        return (self.tx, self.ty) in list(self.head_9by9())

    def is_touching(self, x1:int, y1:int, x2:int, y2:int) -> bool:
        return (x1, y1) in list(self.sq9by9(x2, y2))

    def step(self, direction: str):
        moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        self.hx += moves[direction][0]
        self.hy += moves[direction][1]
        if not self.istouching():
            if self.tx < self.hx:
                self.tx += moves["R"][0]
                self.ty += moves["R"][1]
            elif self.tx > self.hx:
                self.tx += moves["L"][0]
                self.ty += moves["L"][1]

            if self.ty < self.hy:
                self.tx += moves["D"][0]
                self.ty += moves["D"][1]
            elif self.ty > self.hy:
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
                if self.rope[t][0] < self.rope[h][0]:
                    self.rope[t][0] += moves["R"][0]
                    self.rope[t][1] += moves["R"][1]
                elif self.rope[t][0] > self.rope[h][0]:
                    self.rope[t][0] += moves["L"][0]
                    self.rope[t][1] += moves["L"][1]

                if self.rope[t][1] < self.rope[h][1]:
                    self.rope[t][0] += moves["D"][0]
                    self.rope[t][1] += moves["D"][1]
                elif self.rope[t][1] > self.rope[h][1]:
                    self.rope[t][0] += moves["U"][0]
                    self.rope[t][1] += moves["U"][1]

    def addsquare(self, canvas: Canvas, x: int, y: int, mult: int, color):
        x = x * mult
        y = y * mult
        for xx in range(mult):
            for yy in range(mult):
                canvas.set_pixel(x + xx, y + yy, color)


    def PartB(self):
        self.StartPartB()

        positions = set()
        self.rope_length = 10
        self.rope = [[166, 275] for _ in range(self.rope_length)]

        minx = 1_000_000
        maxx = -1_000_000
        miny = 1_000_000
        maxy = -1_000_000

        for line in self.inputdata:
            direction = line.split(" ")[0]
            steps = int(line.split(" ")[1])
            for _ in range(steps):
                self.step_rope(direction)
                positions.add((self.rope[-1][0], self.rope[-1][1]))

                minx = min(minx, self.rope[0][0])
                maxx = max(maxx, self.rope[0][0])
                miny = min(miny, self.rope[0][1])
                maxy = max(maxy, self.rope[0][1])

        print(f"Min: {minx},{miny} Max: {maxx},{maxy}")
        mult = 2
        canvas = Canvas(maxx * mult, maxy * mult)
        for pos in positions:
            self.addsquare(canvas, pos[0], pos[1], mult, (255, 255, 255))
        for pos in self.rope:
            self.addsquare(canvas, pos[0], pos[1], mult, (0, 0, 255))
        self.addsquare(canvas, self.rope[0][0], self.rope[0][1], mult, (255, 0, 0))

        print("Saving")
        canvas.save_PNG("day9.png")

        answer = len(positions)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day9Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

