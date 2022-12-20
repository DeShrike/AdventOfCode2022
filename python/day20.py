from aoc import Aoc
import itertools
import math
import re
import sys

# Day 20
# https://adventofcode.com/2022

class Day20Solution(Aoc):

    def Run(self):
        self.StartDay(20, "Grove Positioning System")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(20)

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
        1
        2
        -3
        3
        -2
        0
        4
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 3

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 1623178306

    def find_solution(self, lijst) -> int:
        count = len(lijst)
        value = 0
        for ix, code in enumerate(lijst):
            if code[0] == 0:
                pos0 = ix
                newpos0 = (pos0 + 1000) % count
                value += lijst[newpos0][0]
                print(f"+1000 = {lijst[newpos0]}")
                newpos0 = (pos0 + 2000) % count
                value += lijst[newpos0][0]
                print(f"+2000 = {lijst[newpos0]}")
                newpos0 = (pos0 + 3000) % count
                value += lijst[newpos0][0]
                print(f"+3000 = {lijst[newpos0]}")
                break

        return value

    def PartA(self):
        self.StartPartA()

        answer = 0

        list1 = [(int(num), ix) for ix, num in enumerate(self.inputdata)]
        list2 = list1[:]
        count = len(list1)
        for ix, code in enumerate(list1):
            num = code[0]
            if num == 0:
                continue
            pos = list2.index(code)
            list2.pop(pos)
            if num > 0:
                newpos = (pos + num) % (count - 1)
            else:
                newpos = (pos + num ) % (count - 1)
            list2.insert(newpos, code)

        answer = self.find_solution(list2)

        # Attempt 1: -19587 is wrong
        # Attempt 2: -17214 is wrong
        # Attempt 3: 805 is too low
        # Attempt 4: 16533 is correct

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = 0
        decryption_key = 811589153

        list1 = [(int(num) * decryption_key, ix) for ix, num in enumerate(self.inputdata)]
        list2 = list1[:]
        count = len(list1)
        for mix in range(10):
            print(f"Mix: {mix}")
            for ix, code in enumerate(list1):
                num = code[0]
                if num == 0:
                    continue
                pos = list2.index(code)
                list2.pop(pos)
                if num > 0:
                    newpos = (pos + num) % (count - 1)
                else:
                    newpos = (pos + num ) % (count - 1)
                list2.insert(newpos, code)

        answer = self.find_solution(list2)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day20Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

