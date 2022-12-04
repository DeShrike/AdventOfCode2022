from aoc import Aoc
import itertools
import math
import re
import sys

# Day 4
# https://adventofcode.com/2022

class Day4Solution(Aoc):

    def Run(self):
        self.StartDay(4, "Camp Cleanup")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(4)

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
        2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 2

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 4

    def PartA(self):
        self.StartPartA()

        answer = 0

        for line in self.inputdata:
            sa, sb = line.split(",")
            a0, a1 = sa.split("-")
            b0, b1 = sb.split("-")
            a0 = int(a0)
            a1 = int(a1)
            b0 = int(b0)
            b1 = int(b1)
            if (b0 <= a0 <= b1 and b0 <= a1 <= b1) or (a0 <= b0 <= a1 and a0 <= b1 <= a1):
                answer += 1

        # Attempt 1 : 455 = too low

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = 0

        for line in self.inputdata:
            sa, sb = line.split(",")
            a0, a1 = sa.split("-")
            b0, b1 = sb.split("-")
            a0 = int(a0)
            a1 = int(a1)
            b0 = int(b0)
            b1 = int(b1)
            if (b0 <= a0 <= b1 or b0 <= a1 <= b1) or (a0 <= b0 <= a1 or a0 <= b1 <= a1):
                answer += 1

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day4Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

