from aoc import Aoc
import itertools
import math
import re
import sys

# Day 18
# https://adventofcode.com/2022

class Day18Solution(Aoc):

    def Run(self):
        self.StartDay(18, "Boiling Boulders")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(18)

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
        2,2,2
        1,2,2
        3,2,2
        2,1,2
        2,3,2
        2,2,1
        2,2,3
        2,2,4
        2,2,6
        1,2,5
        3,2,5
        2,1,5
        2,3,5
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 64

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

    def PartA(self):
        self.StartPartA()

        sides = [
            (-1, 0, 0), (+1, 0, 0),
            (0, -1, 0), (0, +1, 0),
            (0, 0, -1), (0, 0, +1),
        ]

        cubes = {}
        for line in self.inputdata:
            x, y, z = line.strip().split(",")
            x, y, z = int(x), int(y), int(z)
            cubes[(x, y, z)] = True

        answer = 0

        for k in cubes.keys():
            for side in sides:
                sx = k[0] + side[0]
                sy = k[1] + side[1]
                sz = k[2] + side[2]
                if (sx, sy, sz) not in cubes:
                    answer += 1

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day18Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

