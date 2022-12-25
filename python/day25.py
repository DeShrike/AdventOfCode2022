from aoc import Aoc
from utilities import dirange
import itertools
import math
import re
import sys

# Day 25
# https://adventofcode.com/2022

class Day25Solution(Aoc):

    def Run(self):
        self.StartDay(25, "Full of Hot Air")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(25)

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
        1=-0-2
        12111
        2=0=
        21
        2=01
        111
        20012
        112
        1=-1=
        1-12
        12
        1=
        122
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "2=-1=0"

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return None

    def snafu_to_decimal(self, snafu: str) -> int:
        digits = ["2", "1", "0", "-", "="]
        values = [2, 1, 0, -1, -2]
        mult = 1
        result = 0
        for c in dirange(len(snafu) - 1, 0):
            result += values[digits.index(snafu[c])] * mult
            mult *= 5

        return result

    def decimal_to_snafu(self, value: int) -> str:
        digits = ["2", "1", "0", "-", "="]
        values = [2, 1, 0, -1, -2]
        result = ""
        while value > 0:
            v = value % 5
            if v > 2:
                v -= 5
            result = digits[values.index(v)] + result
            value -= v
            value //= 5

        return result

    def PartA(self):
        self.StartPartA()

        total = sum([self.snafu_to_decimal(line.strip()) for line in self.inputdata])
        answer = self.decimal_to_snafu(total)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()
        answer = None
        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day25Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

