from aoc import Aoc
import itertools
import math
import re
import sys

# Day 8
# https://adventofcode.com/2022

class Day8Solution(Aoc):

    def Run(self):
        self.StartDay(8, "Treetop Tree House")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(8)

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
        30373
        25512
        65332
        33549
        35390
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 21

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 8

    def PartA(self):
        self.StartPartA()

        width = len(self.inputdata[0])
        height = len(self.inputdata)
        visible = set()

        for y in range(height):
            for x in range(width):
                tt = int(self.inputdata[y][x])

                # From Left
                rem = self.inputdata[y][:x]
                if all( int(t) < tt for t in rem ):
                    visible.add((x, y))

                # From Right
                rem = self.inputdata[y][x + 1:]
                if all( int(t) < tt for t in rem ):
                    visible.add((x, y))

                # From Top
                rem = [ t[x] for ix, t in enumerate(self.inputdata) if ix < y ]
                if all( int(t) < tt for t in rem ):
                    visible.add((x, y))

                # From Bottom
                rem = [ t[x] for ix, t in enumerate(self.inputdata) if ix > y ]
                if all( int(t) < tt for t in rem ):
                    visible.add((x, y))

        """
        for y in range(height):
            for x in range(width):
                print("V" if (x, y) in visible else ".", end = "")
            print("")
        """
        
        answer = len(visible)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        width = len(self.inputdata[0])
        height = len(self.inputdata)
        scores = []

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                tt = int(self.inputdata[y][x])
                score = 1

                # To Right
                count = 0
                xx = x
                while xx < width - 1:
                	count += 1
                	xx += 1
                	if int(self.inputdata[y][xx]) >= tt:
                		break

                score *= count

                # To Left
                count = 0
                xx = x
                while xx > 0:
                	count += 1
                	xx -= 1
                	if int(self.inputdata[y][xx]) >= tt:
                		break

                score *= count

                # To Bottom
                count = 0
                yy = y
                while yy < height - 1:
                	count += 1
                	yy += 1
                	if int(self.inputdata[yy][x]) >= tt:
                		break

                score *= count

                # To Top
                count = 0
                yy = y
                while yy > 0:
                	count += 1
                	yy -= 1
                	if int(self.inputdata[yy][x]) >= tt:
                		break

                score *= count

                scores.append(score)

        answer = max(scores)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day8Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

