from aoc import Aoc
import itertools
import math
import re
import sys

# Day 5
# https://adventofcode.com/2022

class Day5Solution(Aoc):

    def Run(self):
        self.StartDay(5, "Supply Stacks")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(5)

        goal = self.TestDataA()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)


    def TestDataA(self):
        self.inputdata.clear()
        testdata = \
        """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
        """
        self.inputdata = [line.rstrip() for line in testdata.rstrip().split("\n")]
        return "CMZ"

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return "MCD"

    def parse_data(self):
        max_stacks = 20
        stacks = [[] for _ in range(max_stacks)]
        moves = []  # [(count, from, to), ...]
        inmoves = False
        for line in self.inputdata:
            if line == "":
                inmoves = True
            if inmoves:
                m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
                if m:
                    moves.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))
            else:
                for s in range(max_stacks):
                    ix = s * 4 + 1
                    if ix < len(line) - 1:
                        if line[ix] >= "A" and line[ix] <= "Z":
                            stacks[s].append(line[ix])

        return [list(reversed(stack)) for stack in stacks if len(stack) > 0], moves

    def PartA(self):
        self.StartPartA()

        stacks, moves = self.parse_data()
        for move in moves:
            for _ in range(move[0]):
                container = stacks[move[1] - 1].pop()
                stacks[move[2] - 1].append(container)

        answer = "".join([s.pop() for s in stacks])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        stacks, moves = self.parse_data()

        for move in moves:
            containers = stacks[move[1] - 1][-move[0]:]
            stacks[move[1] - 1] = stacks[move[1] - 1][0:-move[0]]
            _ = [stacks[move[2] - 1].append(container) for container in containers]

        answer = "".join([s.pop() for s in stacks if len(s) > 0])

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day5Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

