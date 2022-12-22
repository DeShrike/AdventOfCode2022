from aoc import Aoc
from canvas import Canvas
import itertools
import math
import re
import sys

# Day 22
# https://adventofcode.com/2022

facings = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Day22Solution(Aoc):

    def Run(self):
        self.StartDay(22, "Monkey Map")
        self.ReadInput()
        self.PartA()
        self.square_size = 50
        self.PartB()

    def Test(self):
        self.StartDay(22)

        goal = self.TestDataA()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB()
        self.square_size = 4
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

    def TestDataA(self):
        self.inputdata.clear()
        testdata = \
        """
        X       ...#
        X       .#..
        X       #...
        X       ....
        ...#.......#
        ........#...
        ..#....#....
        ..........#.
        X       ...#....
        X       .....#..
        X       .#......
        X       ......#.

        10R5L5R10L4R5L5
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 6032

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 5031

    def map_char(self, char:str) -> int:
        if char == "X" or char == " ":
            return 0
        if char == ".":
            return 1
        if char == "#":
            return 2
        raise Exception(f"Unknwon char {char}")

    def parse_input(self):
        inmap = True
        map = []
        steps = []
        for line in self.inputdata:
            if line.strip() == "":
                inmap = False
            else:
                if inmap:
                    row = [self.map_char(c) for c in line]
                    map.append(row)
                else:
                    num = ""
                    for c in line:
                        if c in "LR":
                            if num != "":
                                steps.append(int(num))
                                num = ""
                            steps.append(c)
                        else:
                            num += c
                    if num != "":
                        steps.append(int(num))

        return map, steps

    def move(self, map, x: int, y: int, facing: int):
        nx = x + facings[facing][0]
        ny = y + facings[facing][1]
        if nx < 0:
            nx = len(map[y]) - 1
        if ny < 0:
            ny = len(map) - 1
        if nx >= len(map[y]):
            nx = 0
            while map[y][nx] == 0:
                nx += 1
        if ny >= len(map):
            ny = 0
            while map[ny][x] == 0:
                ny += 1
        while map[ny][nx] == 0:
            nx = nx + facings[facing][0]
            ny = ny + facings[facing][1]
            if ny >= len(map):
                ny = 0
            if nx >= len(map[y]):
                nx = 0
            if nx < 0:
                nx = len(map[y]) - 1
            if ny < 0:
                ny = len(map) - 1
            if map[ny][nx] == 2:
                break
        if map[ny][nx] == 2:
            return x, y        
        else:
            return nx, ny

    def addsquare(self, canvas: Canvas, x: int, y: int, mult: int, color):
        x = x * mult
        y = y * mult
        for xx in range(mult):
            for yy in range(mult):
                canvas.set_pixel(x + xx, y + yy, color)

    def init_canvas(self, canvas, mult, map):
        colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0)]
        height = len(map)
        width = max([len(row) for row in map])
        for py in range(height):
            for px in range(width):
                if px >= len(map[py]):
                    c = 0
                else:
                    c = map[py][px]
                self.addsquare(canvas, px, py, mult, colors[c])

    def PartA(self):
        self.StartPartA()

        map, steps = self.parse_input()
        facing = 0
        height = len(map)
        width = max([len(row) for row in map])
        for y in range(height):
            while len(map[y]) < width:
                map[y].append(0)

        x = map[0].index(1)
        y = 0
        print(f"Start: X: {x}  Y: {y}  Facing: {facing}")

        mult = 2
        canvas = Canvas(width * mult, height * mult)
        self.init_canvas(canvas, mult, map)

        for step in steps:
            if type(step) is int:
                for _ in range(step):
                    x, y = self.move(map, x, y, facing)
                    self.addsquare(canvas, x, y, 2, (0, 255, 0))
            elif step == "R":
                facing = (facing + 1) % len(facings)
            elif step == "L":
                facing = (facing - 1) % len(facings)

        print(f"  End: X: {x}  Y: {y}  Facing: {facing}")
        answer = 1000 * (y + 1) + 4 * (x + 1) + facing

        print(f"Saving")
        canvas.save_PNG("day22a.png")

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        map, steps = self.parse_input()
        facing = 0
        height = len(map)
        width = max([len(row) for row in map])
        for y in range(height):
            while len(map[y]) < width:
                map[y].append(0)

        x = map[0].index(1)
        y = 0
        print(f"Start: X: {x}  Y: {y}  Facing: {facing}")

        mult = 2
        canvas = Canvas(width * mult, height * mult)
        self.init_canvas(canvas, mult, map)

        if self.square_size == 4:
            # Test cube
            edges = [
                { "fromq": (2, 0), "toq": (1, 0), "realq": (1, 1), "x": lambda x: y, "y": lambda y: 0, "facing": lambda f: f - 1 }
                { "fromq": (1, 1), "toq": (1, 0), "realq": (2, 0), "x": lambda x: 0, "y": lambda y: x, "facing": lambda f: f }


                { "fromq": (0, 0), "toq": (0, 0), "realq": (0, 0), "x": lambda x: x, "y": lambda y: y, "facing": lambda f: f }

                { "A1": { "direction": (-1, 0), "quadrant": (1, 0), "swap": False, "rotate": -1 } }
            ]
        else:
            # Real cube
            pass

        for step in steps:
            if type(step) is int:
                for _ in range(step):
                    # x, y = self.move_on_cube(map, x, y, facing)
                    self.addsquare(canvas, x, y, 2, (0, 255, 0))
            elif step == "R":
                facing = (facing + 1) % len(facings)
            elif step == "L":
                facing = (facing - 1) % len(facings)

        print(f"  End: X: {x}  Y: {y}  Facing: {facing}")
        answer = 1000 * (y + 1) + 4 * (x + 1) + facing

        print(f"Saving")
        canvas.save_PNG("day22b.png")

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day22Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

