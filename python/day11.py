from aoc import Aoc
import itertools
import math
import re
import sys

# Day 11
# https://adventofcode.com/2022

class Monkey():
    def __init__(self, id:int):
        self.id = id
        self.divider = None
        self.idtrue = None
        self.iffalse = None
        self.operation_maal = 1 # -1 means square it
        self.operation_plus = 0
        self.items = None
        self.inspections = 0

    def __repr__(self) -> str:
        return f"ID: {self.id}  Items: {self.items}"

    def set_divider(self, divider:int) -> None:
        self.divider = divider

    def set_iftrue(self, val:int) -> None:
        self.iftrue = val

    def set_iffalse(self, val:int) -> None:
        self.iffalse = val

    def set_items(self, items: str) -> None:
        self.items = [int(x) for x in items.split(",")]

    def set_operation(self, maal: int, plus: int) -> None:
        self.operation_maal = maal
        self.operation_plus = plus

class Day11Solution(Aoc):

    def Run(self):
        self.StartDay(11, "Monkey in the Middle")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(11)

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
        Monkey 0:
        Starting items: 79, 98
        Operation: new = old * 19
        Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3

        Monkey 1:
        Starting items: 54, 65, 75, 74
        Operation: new = old + 6
        Test: divisible by 19
            If true: throw to monkey 2
            If false: throw to monkey 0

        Monkey 2:
        Starting items: 79, 60, 97
        Operation: new = old * old
        Test: divisible by 13
            If true: throw to monkey 1
            If false: throw to monkey 3

        Monkey 3:
        Starting items: 74
        Operation: new = old + 3
        Test: divisible by 17
            If true: throw to monkey 0
            If false: throw to monkey 1
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 10605

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

    def parse_input(self):
        mm = {}
        mo = None
        for line in self.inputdata:
            line = line.strip()
            m = re.match(r"Monkey (\d+):", line)
            if m:
                id = int(m.group(1))
                mo = Monkey(id)
                mm[id] = mo
            m = re.match(r"Starting items: (.*)", line)
            if m:
                mo.set_items(m.group(1))
            m = re.match(r"Operation: new = old \* (.*)", line)
            if m:
                if m.group(1) == "old":
                    mo.set_operation(-1, 0)
                else:
                    mo.set_operation(int(m.group(1)), 0)
            m = re.match(r"Operation: new = old \+ (\d*)", line)
            if m:
                mo.set_operation(1, int(m.group(1)))
            m = re.match(r"Test: divisible by (\d*)", line)
            if m:
                mo.set_divider(int(m.group(1)))
            m = re.match(r"If true: throw to monkey (\d*)", line)
            if m:
                mo.set_iftrue(int(m.group(1)))
            m = re.match(r"If false: throw to monkey (\d*)", line)
            if m:
                mo.set_iffalse(int(m.group(1)))
        return mm

    def do_round(self, monkeys):
        for _, m in monkeys.items():
            while len(m.items) > 0:
                item = m.items.pop(0)
                m.inspections += 1
                if m.operation_maal == -1:
                    item = item * item
                else:
                    item = (item * m.operation_maal) + m.operation_plus
                item = item // 3
                if item % m.divider == 0:
                    monkeys[m.iftrue].items.append(item)
                else:
                    monkeys[m.iffalse].items.append(item)
        pass

    def PartA(self):
        self.StartPartA()

        monkeys = self.parse_input()
        #print(monkeys)
        for _ in range(20):
            self.do_round(monkeys)

        # for _, m in monkeys.items():
        #     print(f"{m.id} > {m.inspections}")

        inspected = sorted([m.inspections for _, m in monkeys.items()], reverse=True)
        answer = inspected[0] * inspected[1]

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day11Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

