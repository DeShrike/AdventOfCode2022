from aoc import Aoc
from canvas import Canvas
import itertools
import math
import re
import sys

# Day 14
# https://adventofcode.com/2022

class Day14Solution(Aoc):

    def Run(self):
        self.StartDay(14, "Regolith Reservoir")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(14)

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
        498,4 -> 498,6 -> 496,6
        503,4 -> 502,4 -> 502,9 -> 494,9
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 24

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 93

    def addsquare(self, canvas: Canvas, x: int, y: int, mult: int, color):
        x = x * mult
        y = y * mult
        for xx in range(mult):
            for yy in range(mult):
                canvas.set_pixel(x + xx, y + yy, color)

    def parse_input(self):
        walls = []
        for line in self.inputdata:
            parts = line.strip().split("->")
            x = y = None
            for part in parts:
                tx, ty = part.strip().split(",")
                tx, ty = int(tx), int(ty)
                if x is None:
                    x, y = tx, ty
                    walls.append((x,y))
                else:
                    if x == tx:
                        delta = 1 if ty > y else -1
                        while y != ty:
                            y += delta
                            walls.append((x,y))
                    elif y == ty:
                        delta = 1 if tx > x else -1
                        while x != tx:
                            x += delta
                            walls.append((x,y))

        return walls

    def drop_sand(self, source, walls, sand, height:int):
        x, y = source
        while True:
            newpos = (x, y + 1)
            if newpos not in walls and newpos not in sand:
                x, y = newpos
            else:
                newpos = (x - 1, y + 1)
                if newpos not in walls and newpos not in sand:
                    x, y = newpos
                else:
                    newpos = (x + 1, y + 1)
                    if newpos not in walls and newpos not in sand:
                        x, y = newpos
                    else:
                        return (x, y), False
            if y > height:
                return None, True

    def build_png(self, walls, sand, width:int, height:int, offsetx:int, filename:str) -> None:
        mult = 2
        canvas = Canvas(width * mult, height * mult)
        for w in walls:
            color = 255
            self.addsquare(canvas, w[0] - offsetx, w[1], mult, (color, color, color))
        self.addsquare(canvas, 500 - offsetx, 0, mult, (255, 0, 0))
        for k, _ in sand.items():
            color = 255
            self.addsquare(canvas, k[0] - offsetx, k[1], mult, (color, color, 0))

        print(f"Saving {filename}")
        canvas.save_PNG(filename)

    def PartA(self):
        self.StartPartA()

        source = (500, 0)
        walls = self.parse_input()
        width = max([w[0] for w in walls]) + 10
        height = max([w[1] for w in walls]) + 10
        mx = min([w[0] for w in walls])
        my = min([w[1] for w in walls])
        offsetx = mx - 10
        width -= offsetx
        sand = {}
        print(f"{width}x{height}")
        print(f"{mx}x{my}")

        while True:
            pos, voided = self.drop_sand(source, walls, sand, height)
            if voided:
                break
            l = len(sand)
            if l % 100 == 0:
                print(pos, l)
            sand[pos] = True

        self.build_png(walls, sand, width, height, offsetx, "day14a.png")

        answer = len(sand)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()
        padding = 300
        source = (500, 0)
        walls = self.parse_input()
        width = max([w[0] for w in walls]) + padding + 10
        height = max([w[1] for w in walls]) + 10
        mx = min([w[0] for w in walls])
        my = min([w[1] for w in walls])
        offsetx = 0
        width -= offsetx
        sand = {}
        print(f"{width}x{height}")
        print(f"{mx}x{my}")

        floory = max([w[1] for w in walls]) + 2
        for x in range(10, width - 10):
            walls.append( (x, floory ))

        while True:
            pos, voided = self.drop_sand(source, walls, sand, height)
            if voided:
                break
            if pos == source:
                sand[pos] = True
                break
            l = len(sand)
            if l % 100 == 0:
                print(pos, l)
            sand[pos] = True

        self.build_png(walls, sand, width, height, offsetx, "day14b.png")

        answer = len(sand)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day14Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

