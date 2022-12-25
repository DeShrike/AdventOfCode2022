from aoc import Aoc
import itertools
import math
import re
import sys

# Day 24
# https://adventofcode.com/2022

class Day24Solution(Aoc):

    def Run(self):
        self.StartDay(24, "Blizzard Basin")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(24)

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
        #.######
        #>>.<^<#
        #.<..<<#
        #>v.><>#
        #<^v^^>#
        ######.#
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 18

    def TestDataB(self):
        self.inputdata.clear()
        # self.TestDataA()    # If test data is same as test data for part A
        testdata = \
        """
        1000
        2000
        3000
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

    def parse_input(self):
        map = []
        for line in self.inputdata:
            row = []
            for c in line.strip():
                if c == '#':
                    row.append(0x10)
                elif c == '.':
                    row.append(0x00)
                elif c == '>':
                    row.append(0x01)
                elif c == 'v':
                    row.append(0x02)
                elif c == '<':
                    row.append(0x04)
                elif c == '^':
                    row.append(0x08)
            map.append(row)
        return map

    def move_blizzards(self, map, width: int, height: int):
        dirs = { 0x01: (1, 0), 0x02: (0, 1), 0x04: (-1, 0), 0x08: (0, -1)}
        newmap = [ [ 0 for _ in range(width)] for _ in range(height) ]
        for y, row in enumerate(map):
            for x, b in enumerate(row):
                if b == 0x10:
                    newmap[y][x] = b
                else:
                    if b & 0x01 == 0x01:    # Right ?
                        nx, ny = x + dirs[0x01][0], y + dirs[0x01][1]
                        if map[ny][nx] == 0x10:
                            nx = 1
                        newmap[ny][nx] |= 0x01
                    if b & 0x02 == 0x02:    # Down ?
                        nx, ny = x + dirs[0x02][0], y + dirs[0x02][1]
                        if map[ny][nx] == 0x10:
                            ny = 1
                        newmap[ny][nx] |= 0x02
                    if b & 0x04 == 0x04:    # Left ?
                        nx, ny = x + dirs[0x04][0], y + dirs[0x04][1]
                        if map[ny][nx] == 0x10:
                            nx = width - 2
                        newmap[ny][nx] |= 0x04
                    if b & 0x08 == 0x08:    # Up ?
                        nx, ny = x + dirs[0x08][0], y + dirs[0x08][1]
                        if map[ny][nx] == 0x10:
                            ny = height - 2
                        newmap[ny][nx] |= 0x08

        return newmap

    def print_map(self, map, ex: int, ey: int):
        for y, row in enumerate(map):
            if y > 20:
                break
            for x, b in enumerate(row):
                if x > 40:
                    break
                if (x, y) == (ex, ey):
                    print(u"\u001b[31mE\u001b[0m", end="")
                else:
                    print(".>v+<+++^+++++++#"[b], end="")
            print("")
        print("")

    def move_expedition(self, map, x: int, y: int):
        neightbors = [ (1, 0), (0, 1), (0, -1), (-1, 0) ] # >v^<
        neightbors = [ (1, 0), (0, 1) ] # >v
        # neightbors = [ (1, 0), (0, 1), (0, -1) ] # >v^
        # if y > len(map) // 2:
        #     neightbors = [ (0, 1), (1, 0) ] # v>
        for n in neightbors:
            nx, ny = x + n[0], y + n[1]
            if map[ny][nx] == 0:
                return nx, ny

        if map[y][x] != 0:
            print("oops")
            neightbors = [ (1, 0), (0, 1), (0, -1), (-1, 0) ] # >v^<
            for n in neightbors:
                nx, ny = x + n[0], y + n[1]
                if map[ny][nx] == 0:
                    return nx, ny

        if map[y][x] != 0:
            print("oops 2")

        return x, y

    def PartA(self):
        self.StartPartA()

        answer = None
        map = self.parse_input()
        height = len(map)
        width = len(map[0])
        x = map[0].index(0)
        y = 0
        goalx = map[-1].index(0)
        goaly = len(map) - 1
        print(f"Map: {width} x {height} - Start: {x} x {y} - Goal: {goalx} x {goaly}")

        # self.print_map(map, x, y)
        # a = input()

        steps = 0
        while True:
            steps += 1
            if steps % 100 == 0:
                print(f"Step {steps} Pos: {x} x {y}  ", end = "\r")
            map = self.move_blizzards(map, width, height)
            x, y = self.move_expedition(map, x, y)
            # self.print_map(map, x, y)
            # a = input()
            if (x, y) == (goalx, goaly):
                answer = steps
                break

        # Attempt 1: 511 is too high
        # Attempt 2: 309 is too high
        # Attempt 3: 305 is too high

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day24Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

