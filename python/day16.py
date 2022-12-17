from aoc import Aoc
import itertools
import math
import re
import sys

# Day 16
# https://adventofcode.com/2022

class Valve():
    def __init__(self, id:str, flowrate:int, other):
        self.id = id
        self.flowrate = flowrate
        self.other = other
        self.paths = [v.strip() for v in other.split(",")]

    def __repr__(self):
        return f"Valve('{self.id}', {self.flowrate}, {self.paths})"

class Day16Solution(Aoc):

    def Run(self):
        self.StartDay(16, "Proboscidea Volcanium")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(16)

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
        Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
        Valve BB has flow rate=13; tunnels lead to valves CC, AA
        Valve CC has flow rate=2; tunnels lead to valves DD, BB
        Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
        Valve EE has flow rate=3; tunnels lead to valves FF, DD
        Valve FF has flow rate=0; tunnels lead to valves EE, GG
        Valve GG has flow rate=0; tunnels lead to valves FF, HH
        Valve HH has flow rate=22; tunnel leads to valve GG
        Valve II has flow rate=0; tunnels lead to valves AA, JJ
        Valve JJ has flow rate=21; tunnel leads to valve II
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 1651

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
        valves = {}
        for line in self.inputdata:
            m = re.match(r"Valve (.*) has flow rate=(\d+); tunnel(s?) lead(s?) to valve(s?) (.*)", line)
            if m:
                id = m.group(1)
                flowrate = int(m.group(2))
                other = m.group(6)
                valves[id] = Valve(id, flowrate, other)

        return valves

    def PartA(self):
        self.StartPartA()

        valves = self.parse_input()
        for _, valve in valves.items():
            if valve.flowrate > 0:
                print(valve)
        print(len(valves))

        # Add solution here

        answer = None

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day16Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

