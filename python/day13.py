from aoc import Aoc
import itertools
import math
import re
import sys

# Day 13
# https://adventofcode.com/2022

class Packet():
    def __init__(self, line:str):
        self.value = None
        self.array = []
        self.empty = False
        self.parse(line)
    
    def __str__(self) -> str:
        if self.empty:
            return ""
        elif self.value is not None:
            return str(self.value)
        else:
            return "[" + ",".join([str(i) for i in  self.array]) + "]"

    def split(self, line:str):
        ina = 0
        result = ""
        for ch in line:
            if ch == "[":
                ina += 1
                result += ch
            elif ch == "]":
                ina -= 1
                result += ch
            elif ch == ",":
                if ina > 0:
                    result += ";"
                else:
                    result += ch
            else:
                result += ch
                
        return [s.replace(";", ",") for s in result.split(",")]

    def parse(self, line:str) -> None:
        if line == "":
            self.empty = True
        elif line.isnumeric():
            self.value = int(line)
        elif line[0] == "[" and line[-1] == "]":
            line = line[1:-1]
            parts = self.split(line)
            for part in parts:
                self.array.append(Packet(part))


class Day13Solution(Aoc):

    def Run(self):
        self.StartDay(13, "AOC")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(13)

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
        [1,1,3,1,1]
        [1,1,5,1,1]

        [[1],[2,3,4]]
        [[1],4]

        [9]
        [[8,7,6]]

        [[4,4],4,4]
        [[4,4],4,4,4]

        [7,7,7,7]
        [7,7,7]

        []
        [3]

        [[[]]]
        [[]]

        [1,[2,[3,[4,[5,6,7]]]],8,9]
        [1,[2,[3,[4,[5,6,0]]]],8,9]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 13

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

        self.inputdata.append("")
        pairs = []
        pl = None
        pr = None
        for line in self.inputdata:
            line = line.strip()
            if line == "":
                pp = { "left": pl, "right": pr }
                pl = pr = None
                pairs.append(pp)
            else:
                p = Packet(line)
                if pl == None:
                    pl = p
                else:
                    pr = p

        for pair in pairs:
            print(f"Left: {str(pair['left'])}")
            print(f"Right: {str(pair['right'])}")
            print("")

        # Add solution here

        answer = None

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day13Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

