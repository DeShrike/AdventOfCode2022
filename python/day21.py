from aoc import Aoc
import itertools
import math
import re
import sys

# Day 21
# https://adventofcode.com/2022

class Monkey():
    def __init__(self, name: str, value: int, left, right, operation: str):
        self.name = name
        self.value = value
        self.left = left
        self.right = right
        self.operation = operation

    def __repr__(self):
        return f"Monkey({self.name}, {self.value}, {self.left}, {self.right}, {self.operation})"

    def get_value(self, monkeys) -> int:
        if self.value is not None:
            return self.value
        else:
            mleft = [m for m in monkeys if m.name == self.left][0]
            mright = [m for m in monkeys if m.name == self.right][0]
            if self.operation == "+":
                return mleft.get_value(monkeys) + mright.get_value(monkeys)
            if self.operation == "-":
                return mleft.get_value(monkeys) - mright.get_value(monkeys)
            if self.operation == "*":
                return mleft.get_value(monkeys) * mright.get_value(monkeys)
            if self.operation == "/":
                return mleft.get_value(monkeys) // mright.get_value(monkeys)
            return None

    def equal(self, monkeys) -> bool:
        mleft = [m for m in monkeys if m.name == self.left][0]
        mright = [m for m in monkeys if m.name == self.right][0]
        return mleft.get_value(monkeys) == mright.get_value(monkeys)

class Day21Solution(Aoc):

    def Run(self):
        self.StartDay(21, "Monkey Math")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(21)

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
        root: pppw + sjmn
        dbpl: 5
        cczh: sllz + lgvd
        zczc: 2
        ptdq: humn - dvpt
        dvpt: 3
        lfqf: 4
        humn: 5
        ljgn: 2
        sjmn: drzm * dbpl
        sllz: 4
        pppw: cczh / lfqf
        lgvd: ljgn * ptdq
        drzm: hmdt - zczc
        hmdt: 32
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 152

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 301

    def parse_input(self):
        monkeys = []
        for line in self.inputdata:
            m = re.match(r"(.{4}): (\d+)", line)
            if m:
                name = m.group(1)
                value = int(m.group(2))
                m = Monkey(name, value, None, None, None)
                monkeys.append(m)
            else:
                m = re.match(r"(.{4}): (.{4}) (.{1}) (.{4})", line)
                if m:
                    name = m.group(1)
                    left = m.group(2)
                    right = m.group(4)
                    operation = m.group(3)
                    m = Monkey(name, None, left, right, operation)
                    monkeys.append(m)

        return monkeys

    def PartA(self):
        self.StartPartA()

        monkeys = self.parse_input()
        root = [m for m in monkeys if m.name == "root"][0]

        answer = root.get_value(monkeys)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        monkeys = self.parse_input()
        root = [m for m in monkeys if m.name == "root"][0]
        humn = [m for m in monkeys if m.name == "humn"][0]
        print(root)
        m1 = [m for m in monkeys if m.name == root.left][0]
        m2 = [m for m in monkeys if m.name == root.right][0]
        print(humn)
        print(m1)
        print(m2)

        v2 = m2.get_value(monkeys)

        answer = None

        value = 3_555_057_453_200
        while value < 3_555_057_453_300:
            humn.value = value
            v1 = m1.get_value(monkeys)
            print(f"{value}\t{v1}\t{v2}\t{v1 - v2}")
            value += 1
            if v1 == v2:
                answer = value
                break

        # Attempt 1: 3555057453233 is too high

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day21Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

