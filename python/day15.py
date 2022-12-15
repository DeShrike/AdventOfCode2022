from aoc import Aoc
import itertools
import math
import re
import sys

# Day 15
# https://adventofcode.com/2022

def distt(x1:int, y1:int, x2:int, y2:int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

def dist(p1, p2) -> int:
    return distt(*p1, *p2)

class Sensor():
    def __init__(self, pos, beacon):
        self.pos = pos
        self.beacon = beacon
        self.distance = dist(self.pos, self.beacon)

    def __repr__(self):
        return f"Sensor({self.pos}, {self.beacon}) ({'+' if self.beacon[0] > self.pos[0] else '-'} {'+' if self.beacon[1] > self.pos[1] else '-'}) -> {self.distance}"

class Day15Solution(Aoc):

    def Run(self):
        self.StartDay(15, "Beacon Exclusion Zone")
        self.ReadInput()
        self.row_to_test = 2_000_000
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(15)

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
        Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        Sensor at x=9, y=16: closest beacon is at x=10, y=16
        Sensor at x=13, y=2: closest beacon is at x=15, y=3
        Sensor at x=12, y=14: closest beacon is at x=10, y=16
        Sensor at x=10, y=20: closest beacon is at x=10, y=16
        Sensor at x=14, y=17: closest beacon is at x=10, y=16
        Sensor at x=8, y=7: closest beacon is at x=2, y=10
        Sensor at x=2, y=0: closest beacon is at x=2, y=10
        Sensor at x=0, y=11: closest beacon is at x=2, y=10
        Sensor at x=20, y=14: closest beacon is at x=25, y=17
        Sensor at x=17, y=20: closest beacon is at x=21, y=22
        Sensor at x=16, y=7: closest beacon is at x=15, y=3
        Sensor at x=14, y=3: closest beacon is at x=15, y=3
        Sensor at x=20, y=1: closest beacon is at x=15, y=3
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        self.row_to_test = 11
        return 26

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 56000011

    def parse_input(self):
        sensors = []
        for line in self.inputdata:
            line = line.strip()
            m = re.match(r"Sensor at x=([\-0-9]+), y=([\-0-9]+): closest beacon is at x=([\-0-9]+), y=([\-0-9]+)", line)
            if m:
                sx = int(m.group(1))
                sy = int(m.group(2))
                bx = int(m.group(3))
                by = int(m.group(4))
                sensors.append(Sensor((sx, sy), (bx, by)))

        return sensors

    def calc_stukken(self, sensors):
        stukken = []
        for ix, s in enumerate(sensors):
            elevation = abs(s.pos[1] - self.row_to_test)
            print(f"{ix} -> {elevation}")
            if s.distance - elevation < 0:
                continue
            stuk = (s.pos[0] - (s.distance - elevation), s.pos[0] + (s.distance - elevation))
            if stuk[1] < stuk[0]:
                stuk = (stuk[1], stuk[0])
            stukken.append(stuk)
        
        stukken.sort(key=lambda x: x[0])
        # print(stukken)
        return stukken

    def calc_runs(self, stukken)
        runs = []
        vanaf = stukken[0][0]
        running = stukken[0][1]
        for stuk in stukken[1:]:
            if vanaf <= stuk[0] <= running:
                running = max(running, stuk[1])
            else:
                runs.append((vanaf, running))
                vanaf = stuk[0]
                running = stuk[1]
        runs.append((vanaf, running))
        return runs

    def PartA(self):
        self.StartPartA()

        sensors = self.parse_input()
        # for ix, s in enumerate(sensors):
        #     print(ix, s)

        stukken = self.calc_stukken(sensors)
        runs = self.calc_runs(stukken)

        # print("Runs:")
        # print(runs)

        # positions = 0
        # for run in runs:
        #     print(f"{run} Run size: {run[1] - run[0] + 1}")
        #     positions += (run[1] - run[0] + 1)

        # print(f"Positions A: {positions}")

        beaconsonrow = set()
        for s in sensors:
            if s.beacon[1] == self.row_to_test:
                beaconsonrow.add(s.beacon)

        # print(f"beaconsonrow: {beaconsonrow}")

        positions -= len(beaconsonrow)

        # print(f"Positions B: {positions}")

        answer = positions

        # for y in range(-12, 28):
        #     print(f"{y:3} ", end="")
        #     count = 0
        #     for x in range(-10, 30):
        #         letter = "."
        #         for ix, s in enumerate(sensors):
        #             if ix != 4:
        #                 continue
        #             if s.pos == (x, y):
        #                 letter = "S"
        #             elif s.beacon == (x,y):
        #                 letter = 'B'
        #             elif dist(s.pos, (x, y)) <= s.distance:
        #                 letter = "+"
        #         count += 1 if letter == "+" else 0
        #         print(letter, end="")
        #     print(f"  -> {count}")

        # Attempt 1: 6438941 is too high

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        sensors = self.parse_input()

        for y in range(4_000_000):
            if y % 100 == 0:
                print(y)
            self.row_to_test = y
            stukken = self.calc_stukken(sensors)
            runs = self.calc_runs(stukken)
            if len(runs) > 1:
                print(runs)
                break

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day15Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

