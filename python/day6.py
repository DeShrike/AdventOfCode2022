from aoc import Aoc
import itertools
import math
import re
import sys

# Day 6
# https://adventofcode.com/2022

class Day6Solution(Aoc):

    def Run(self):
        self.StartDay(6, "Tuning Trouble")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(6)

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
        zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 11

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 26

    def PartA(self):
        self.StartPartA()

        answer = None

        for ix in range(len(self.inputdata[0]) - 4):
            if len(list(set(self.inputdata[0][ix:ix + 4]))) == 4:
                answer = ix + 4
                break

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = None

        for ix in range(len(self.inputdata[0]) - 14):
            if len(list(set(self.inputdata[0][ix:ix + 14]))) == 14:
                answer = ix + 14
                break

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day6Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

