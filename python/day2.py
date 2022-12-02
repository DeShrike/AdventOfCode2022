from aoc import Aoc
import itertools
import math
import re
import sys

# Day 2
# https://adventofcode.com/2022

class Day2Solution(Aoc):

    def Run(self):
        self.StartDay(2, "Rock Paper Scissors")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(2)

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
        A Y
        B X
        C Z
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 15

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 12

    def PartA(self):
        self.StartPartA()

        they = [ 'A', 'B', 'C' ]
        us = [ 'X', 'Y', 'Z' ]
        beats = [(0,2), (2,1), (1,0)]

        answer = 0
        for line in self.inputdata:
            t, u = line.split(' ')
            tix = they.index(t)
            uix = us.index(u)
            if tix == uix:
                answer += uix + 1 + 3
            else:
                answer += uix + 1 + (6 if ((uix, tix) in beats) else 0)

        # Attempt 1 : 11756 = too low

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        they = [ 'A', 'B', 'C' ]
        us = [ 'X', 'Y', 'Z' ]
        goal = [ 0,  3,  6]
        towin = { 0:2, 2:1, 1:0 }
        toloose = { 0:1, 2:0, 1:2 }
        answer = 0
        for line in self.inputdata:
            t, u = line.split(' ')
            tix = they.index(t)
            uix = us.index(u)
            g = goal[uix]
            if g == 3:      # draw
                uix = tix
            elif g == 0:    # loose
                uix = towin[tix]
            else:           # win
                uix = toloose[tix]
            answer += uix + 1 + g

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day2Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

