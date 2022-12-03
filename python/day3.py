from aoc import Aoc
import itertools
import math
import re
import sys

# Day 3
# https://adventofcode.com/2022

class Day3Solution(Aoc):

    def Run(self):
        self.StartDay(3, "Rucksack Reorganization")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(3)

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
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 157

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

    def prio(self, letter:str) -> int:
        return ord(letter) - 38 if ord(letter) <= 90 else ord(letter) - 96

    def PartA(self):
        self.StartPartA()

        answer = 0
        for line in self.inputdata:
            c = len(line) // 2
            c1 = set(line[0:c])
            c2 = set(line[c:])
            common = list(c1.intersection(c2))[0]
            answer += self.prio(common)
        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day3Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

