from aoc import Aoc
import itertools
import math
import re
import sys

# Day 1
# https://adventofcode.com/2022

class Day1Solution(Aoc):

    def Run(self):
        self.StartDay(1, "Calorie Counting")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(1)

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
        1000
        2000
        3000

        4000

        5000
        6000

        7000
        8000
        9000

        10000
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 24000

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 45000

    def PartA(self):
        self.StartPartA()

        elves = []
        count = 0
        for line in self.inputdata:
            if line == "":
                elves.append(count)
                count = 0
            else:
                count += int(line)
        elves.append(count)

        answer = sorted(elves)[-1]

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        elves = []
        count = 0
        for line in self.inputdata:
            if line == "":
                elves.append(count)
                count = 0
            else:
                count += int(line)
        elves.append(count)

        answer = sorted(elves)[-1] + sorted(elves)[-2] + sorted(elves)[-3]

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day1Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

