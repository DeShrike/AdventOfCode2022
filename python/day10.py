from aoc import Aoc
import itertools
import math
import re
import sys

# Day 10
# https://adventofcode.com/2022

class Day10Solution(Aoc):

    def Run(self):
        self.StartDay(10, "Cathode-Ray Tube")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(10)

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
        addx 15
        addx -11
        addx 6
        addx -3
        addx 5
        addx -1
        addx -8
        addx 13
        addx 4
        noop
        addx -1
        addx 5
        addx -1
        addx 5
        addx -1
        addx 5
        addx -1
        addx 5
        addx -1
        addx -35
        addx 1
        addx 24
        addx -19
        addx 1
        addx 16
        addx -11
        noop
        noop
        addx 21
        addx -15
        noop
        noop
        addx -3
        addx 9
        addx 1
        addx -3
        addx 8
        addx 1
        addx 5
        noop
        noop
        noop
        noop
        noop
        addx -36
        noop
        addx 1
        addx 7
        noop
        noop
        noop
        addx 2
        addx 6
        noop
        noop
        noop
        noop
        noop
        addx 1
        noop
        noop
        addx 7
        addx 1
        noop
        addx -13
        addx 13
        addx 7
        noop
        addx 1
        addx -33
        noop
        noop
        noop
        addx 2
        noop
        noop
        noop
        addx 8
        noop
        addx -1
        addx 2
        addx 1
        noop
        addx 17
        addx -9
        addx 1
        addx 1
        addx -3
        addx 11
        noop
        noop
        addx 1
        noop
        addx 1
        noop
        noop
        addx -13
        addx -19
        addx 1
        addx 3
        addx 26
        addx -30
        addx 12
        addx -1
        addx 3
        addx 1
        noop
        noop
        noop
        addx -9
        addx 18
        addx 1
        addx 2
        noop
        noop
        addx 9
        noop
        noop
        noop
        addx -1
        addx 2
        addx -37
        addx 1
        addx 3
        noop
        addx 15
        addx -21
        addx 22
        addx -6
        addx 1
        noop
        addx 2
        addx 1
        noop
        addx -10
        noop
        noop
        addx 20
        addx 1
        addx 2
        addx 2
        addx -6
        addx -11
        noop
        noop
        noop
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 13140

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return None

    def PartA(self):
        self.StartPartA()

        answer = 0
        X = 1
        cycle = 0
        for line in self.inputdata:
            if line == "noop":
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    print(f"Cycle {cycle}: {X}     {(cycle * X)}")
                    answer += (cycle * X)
            else:
                value = int(line.split(" ")[1])
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    print(f"Cycle {cycle}: {X}    {(cycle * X)}")
                    answer += (cycle * X)
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    print(f"Cycle {cycle}: {X}    {(cycle * X)}")
                    answer += (cycle * X)
                X += value

        self.ShowAnswer(answer)

    def do_cycle(self, screen, x:int, y:int, X:int, cycle:int, width:int) -> int:
        if X == x - 1 or X == x or X == x + 1:
            screen[y][x] = 1
        cycle += 1
        x += 1
        if x >= width:
            x = 0
            y += 1
        return cycle, x, y

    def PartB(self):
        self.StartPartB()

        X = 1
        cycle = 0
        width = 40
        height = 6
        x = 0
        y = 0
        screen = [[ 0 for _ in range(width)] for _ in range(height)]

        for line in self.inputdata:
            if line == "noop":
                cycle, x, y = self.do_cycle(screen, x, y, X, cycle, width)
            else:
                value = int(line.split(" ")[1])
                cycle, x, y = self.do_cycle(screen, x, y, X, cycle, width)
                cycle, x, y = self.do_cycle(screen, x, y, X, cycle, width)
                X += value

        for y in range(height):
            for x in range(width):
                print("#" if screen[y][x] else ".", end="")
            print("")

        answer = "BACEKLHF"

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day10Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

