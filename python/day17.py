from errno import ENETRESET
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

        checkheight = 2
        checkstart = checkheight

        for _ in range(self.rocks_to_fall):
            self.fall_rock()
            # print("********************************************************")
            # print(f"Grid: {self.width}, {self.height}   Tall: {self.tall}")
            # for i in range(self.height - 1, -1, -1):
            #     for j in range(self.width):
            #         print(".#@$&%£"[self.grid[i][j]], end="")
            #     print("")
            # a = input()
            checkstart += 1

        answer = self.tall

        # for i in range(self.height - 1, -1, -1):
        #     print(f"{i:5} ", end="")
        #     for j in range(self.width):
        #         print(".#@$&%£"[self.grid[i][j]], end="")
        #     print("")

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        """
        # Test:
        # 35 blokken in 53 lijnen
        # 15 extra = 24 lijnen

        r = self.rocks_to_fall // 35
        totaal_lijnen = r * 53 + 24 + 1

        # Echte:
        # X blokken in 2534 lijnen
        # X extra = 495 lijnen
        """

        answer = None
        self.width = 7
        self.height = 0
        self.tall = 0
        self.grid = [[0 for _ in range(self.width)] for _ in range(7)]
        self.height = len(self.grid)
        self.windindex = 0
        self.rock_index = 0

        exta = 494
        repeat = 2634

        # exta = 25
        # repeat = 53

        extra_blocks = 0
        repeat_blocks = 0
        for rockcount in range(10_000):
            self.fall_rock()
            if self.tall > exta + 1:
                if extra_blocks == 0:
                    print(f"exta: {self.tall} {self.grid[self.tall-1]}")
                    extra_blocks = rockcount - 1
            if self.tall >= exta + repeat + 1:
                if repeat_blocks == 0:
                    print(self.grid[self.tall-1])
                    print(f"Tall: {self.tall}   exta + repeat + 1:{exta + repeat + 1}")
                    repeat_blocks = rockcount - extra_blocks
                    break
        
        #fallen = extra_blocks + 

        print(f"Extra Block: {extra_blocks}")
        print(f"Repeat Block: {repeat_blocks}")

        r = self.rocks_to_fall // repeat_blocks
        totaal_lijnen = r * repeat + exta + 1

        answer = totaal_lijnen - 1

        # for i in range(self.height - 1, -1, -1):
        #     for j in range(self.width):
        #         print(".#@$&%£"[self.grid[i][j]], end="")
        #     print("")

        # Attempt 1: 1548899754056 is too low
        # Attempt 2: 1548899754057 is too low
        # Attempt 3: 1553982300128 is too low
        # Attempt 4: 1554899645942 is wrong 

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day17Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

