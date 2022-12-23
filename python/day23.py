from aoc import Aoc
import itertools
import math
import re
import sys

# Day 23
# https://adventofcode.com/2022

dirs = [
    [ (0, -1), (-1, -1), (1, -1) ],
    [  (0, 1),  (-1, 1),  (1, 1) ],
    [ (-1, 0), (-1, -1), (-1, 1) ],
    [  (1, 0),  (1, -1),  (1, 1) ]
]

class Day23Solution(Aoc):

    def Run(self):
        self.StartDay(23, "Unstable Diffusion")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(23)

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
        ..............
        ..............
        .......#......
        .....###.#....
        ...#...#.#....
        ....#...##....
        ...#.###......
        ...##.#.##....
        ....#..#......
        ..............
        ..............
        ..............
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 110

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 20

    def parse_input(self):
        elves = []
        for y, line in enumerate(self.inputdata):
            row = []
            for x, c in enumerate(line.strip()):
                if c == "#":
                    elves.append((x,y))
        return elves

    def show_elves(self, elves):
        minx = min([ e[0] for e in elves ])
        maxx = max([ e[0] for e in elves ])
        miny = min([ e[1] for e in elves ])
        maxy = max([ e[1] for e in elves ])
        
        print("    ", end="")
        for x in range(minx, maxx + 1):
            print( abs(x) % 10 , end="")
        print("")
        for y in range(miny, maxy + 1):
            print(f"{y:3} ", end="")
            for x in range(minx, maxx + 1):
                print("#" if (x, y) in elves else ".", end="")
            print("")
        print("")

    def contains_elve(self, elves, posses):
        for pos in posses:
            if pos in elves:
                return True
        return False

    def has_neighbors(self, elves, elve):
        neighbors = [(-1, 0), (-1, -1,), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        for n in neighbors:
            if (elve[0] + n[0], elve[1] + n[1]) in elves:
                return True
        return False

    def do_round(self, elves, dirindex: int):
        possible_moves = [] # [[oldpos, newpos], ... ]
        newelves = []
        moved = False
        elves_dict = { e: True for e in elves }
        for elve in elves:
            if self.has_neighbors(elves_dict, elve) == False:
                newelves.append(elve)
            else:    
                newpos = None
                for diroffset in range(4):
                    ddd = dirs[(dirindex + diroffset) % len(dirs)]
                    newposses = [ (elve[0] + d[0], elve[1] + d[1]) for d in ddd]
                    if self.contains_elve(elves_dict, newposses) == False:
                        newpos = (elve[0] + ddd[0][0], elve[1] + ddd[0][1])
                        possible_moves.append([elve, newpos])
                        break
                if newpos is None:
                    newelves.append(elve)

        for pm in possible_moves:
            oe = pm[0]
            ne = pm[1]
            if len([ p for p in possible_moves if p[1] == ne ]) == 1:
                moved = True
                newelves.append(ne)
            else:
                newelves.append(oe)

        return newelves, moved

    def PartA(self):
        self.StartPartA()

        dirindex = 0
        elves = self.parse_input()

        # print("== Initial State ==")
        # self.show_elves(elves)

        for round in range(10):
            print(f"Round {round + 1}", end="\r")
            elves, _ = self.do_round(elves, dirindex)
            dirindex = (dirindex + 1) % len(dirs)
            # print(f"== End of Round {round + 1} ==")
            # self.show_elves(elves)
            # a = input()

        answer = 0

        minx = min([ e[0] for e in elves ])
        maxx = max([ e[0] for e in elves ])
        miny = min([ e[1] for e in elves ])
        maxy = max([ e[1] for e in elves ])
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                if (x, y) not in elves:
                    answer += 1

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = None

        dirindex = 0
        elves = self.parse_input()

        for round in range(10000):
            print(f"Round {round + 1}", end="\r")
            elves, moved = self.do_round(elves, dirindex)
            dirindex = (dirindex + 1) % len(dirs)
            if moved == False:
                answer = round + 1
                break

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day23Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

