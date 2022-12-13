from struct import pack
from aoc import Aoc
import itertools
import math
import re
import sys

# Day 13
# https://adventofcode.com/2022

class Packet():
    def __init__(self, line:str, marker:bool = False):
        self.value = None
        self.array = []
        self.empty = False
        self.parse(line)
        self.forcefalse = False
        self.parent = None
        self.marker = marker

    def __str__(self) -> str:
        if self.empty:
            return "E"
        elif self.value is not None:
            return str(self.value)
        else:
            return "[" + ",".join([str(i) for i in  self.array]) + "]"

    def convert_to_array(self):
        p = Packet(f"{self.value}")
        p.parent = self
        self.array.append(p)
        self.value = None

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
                p = Packet(part)
                p.parent = self
                self.array.append(p)

    def __lt__(self, other):
        # print(f"Compare: {self} v {other}")
        # a = input()
        if self.empty and not other.empty:
            return True
        elif not self.empty and other.empty:
            self.forcefalse = True
            if self.parent is not None:
                self.parent.forcefalse = True
            return False
        elif self.value is not None and other.value is not None:
            if self.value > other.value:
                self.parent.forcefalse = True
                # print("set forcefalse")
            return self.value < other.value
        elif self.value is None and other.value is not None:
            # convert other to list
            other.convert_to_array()
            return self < other
        elif self.value is not None and other.value is None:
            # convert self to list
            self.convert_to_array()
            return self < other
        else:
            # print("zipping")
            for a, b in zip(self.array, other.array):
                if a < b:
                    return True
                if self.forcefalse:
                    if self.parent is not None:
                        self.parent.forcefalse = True
                    # print("forcefalse")
                    return False
            if len(self.array) < len(other.array):
                # print(f"array smaller  {len(self.array)} v {len(other.array)}")
                return True
            elif len(self.array) > len(other.array):
                self.forcefalse = True
                if self.parent is not None:
                    self.parent.forcefalse = True

            return False
        
class Day13Solution(Aoc):

    def Run(self):
        self.StartDay(13, "Distress Signal")
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
        self.TestDataA()
        return 140

    def PartA(self):
        self.StartPartA()

        answer = None
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

        # print(len(pairs))

        # for pair in pairs:
        #     print(f"Left: {str(pair['left'])}")
        #     print(f"Right: {str(pair['right'])}")
        #     print("")

        # Add solution here
        # for i in range(len(pairs)):
            # i = 81 ???  138 ????
        # i = 138
        # print(f"*************************************** {i}")
        # a = input()
        # t = i + 1
        # if pairs[t - 1]["left"] < pairs[t - 1]["right"]:
        #     print("Smaller")
        # else:
        #     print("NOT smaller")

        # sm = [ ix + 1 for ix, p in enumerate(pairs) if p["left"] < p["right"]]
        # print(sm)
        answer = sum([ ix + 1 for ix, p in enumerate(pairs) if p["left"] < p["right"]])

        # Attempt 1: 7854 is too high
        # Attempt 2: 6240 is too high

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        packets = []
        for line in self.inputdata:
            line = line.strip()
            if line != "":
                packets.append(Packet(line))

        packets.append(Packet("[[2]]", True))
        packets.append(Packet("[[6]]", True))

        # print(len(packets))
        
        # Bubblesort
        switched = True
        while switched:
            switched = False
            for i in range(len(packets) - 1):
                if packets[i + 1] < packets[i]:
                    packets[i], packets[i + 1] = packets[i + 1], packets[i]
                    switched = True

        answer = 1
        for ix, p in enumerate(packets):
            if p.marker:
                answer *= (ix + 1)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day13Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

