from aoc import Aoc
import itertools
import math
import re
import sys

# Day 17
# https://adventofcode.com/2022

rocks = [
    ####
    [(0,0), (1,0), (2,0), (3,0)],

     # 
    ###
     # 
    [(1,0), (0,1), (1,1), (2,1), (1,2)],

    #   #
    #   #
    # ###
    # [(2,0), (2,1), (2,2), (0,2), (1,2)],

    ###
      #
      #
    [(0,0), (1,0), (2,0), (2,1), (2,2)],

    #
    #
    #
    #
    [(0,0), (0,1), (0,2), (0,3)],

    ##
    ##
    [(0,0), (1,0), (0,1), (1,1)]
]

class Day17Solution(Aoc):

    def Run(self):
        self.StartDay(17, "Pyroclastic Flow")
        self.ReadInput()
        self.rocks_to_fall = 2022
        self.PartA()
        self.rocks_to_fall = 1_000_000_000_000
        self.PartB()

    def Test(self):
        self.StartDay(17)

        goal = self.TestDataA()
        self.rocks_to_fall = 2022
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB()
        self.rocks_to_fall = 1_000_000_000_000
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

    def TestDataA(self):
        self.inputdata.clear()
        testdata = \
        """
        >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 3068

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 1514285714288

    def get_wind_dir(self):
        char = self.inputdata[0][self.windindex]
        self.windindex = (self.windindex + 1) % len(self.inputdata[0])
        return -1 if char == "<" else 1
    
    def place_rock(self, x:int, y:int, rock):
        for p in rock:
            rx = x + p[0]
            ry = y + p[1]
            while ry >= self.height:
                self.grid.append( [0 for _ in range(self.width)] )
                self.height += 1
            self.grid[ry][rx] = 1 + self.rock_index
            self.tall = max(ry + 1, self.tall)

    def can_move(self, x:int, y:int, rock):
        for p in rock:
            rx, ry = p
            rx += x
            ry += y
            if rx < 0 or rx >= self.width:
                return False
            if ry < 0:
                return False
            if ry >= self.height:
                continue
            if self.grid[ry][rx] != 0:
                return False
        return True

    def fall_rock(self):
        rock = rocks[self.rock_index]
        self.rock_index = (self.rock_index + 1) % len(rocks)
        x = 2
        # y = self.tall + 3 + max([ r[1] for r in rock ])
        y = self.tall + 3
        # print(f"Start: {x}, {y}")
        while True:
            winddir = self.get_wind_dir()
            # print(f"Wind: {winddir}")
            if self.can_move(x + winddir, y, rock):
                x += winddir
            if self.can_move(x, y - 1, rock):
                y -= 1
            else:
                break
        self.place_rock(x, y, rock) 

    def PartA(self):
        self.StartPartA()

        answer = None
        self.width = 7
        self.height = 0
        self.tall = 0
        self.grid = [[0 for _ in range(self.width)] for _ in range(7)]
        self.height = len(self.grid)
        self.windindex = 0
        self.rock_index = 0
        for _ in range(self.rocks_to_fall):
            self.fall_rock()
            # print("********************************************************")
            # print(f"Grid: {self.width}, {self.height}   Tall: {self.tall}")
            # for i in range(self.height - 1, -1, -1):
            #     for j in range(self.width):
            #         print(".#@$&%£"[self.grid[i][j]], end="")
            #     print("")
            # a = input()
        answer = self.tall

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day17Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

