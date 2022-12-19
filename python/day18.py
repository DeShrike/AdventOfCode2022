from aoc import Aoc
import itertools
import math
import re
import sys

# Day 18
# https://adventofcode.com/2022

sides = [
    (-1, 0, 0), (+1, 0, 0),
    (0, -1, 0), (0, +1, 0),
    (0, 0, -1), (0, 0, +1),
]

class Day18Solution(Aoc):

    def Run(self):
        self.StartDay(18, "Boiling Boulders")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(18)

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
        2,2,2
        1,2,2
        3,2,2
        2,1,2
        2,3,2
        2,2,1
        2,2,3
        2,2,4
        2,2,6
        1,2,5
        3,2,5
        2,1,5
        2,3,5
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 64

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 58

    def sides_occupied(self, cubes, x:int, y:int, z:int) -> int:
        return len([1 for side in sides if (x + side[0], y + side[1], z + side[2]) not in cubes])

    def sides_occupied_2(self, cubes, x:int, y:int, z:int) -> int:
        return len([1 for side in sides if (x + side[0], y + side[1], z + side[2]) in cubes])

    def open_to_airX(self, cubes, x:int, y:int, z:int) -> bool:
        for side in sides:
            nx = x + side[0] 
            ny = y + side[1] 
            nz = z + side[2] 
            if (nx, ny, nz) not in cubes:
                while True:
                    nx += side[0]
                    ny += side[1]
                    nz += side[2]
                    if (nx, ny, nz) in cubes:
                        break
                    if abs(nx) > 100 or abs(ny) > 100 or abs(nz) > 100:
                        return True
        return False

    def open_to_air(self, cubes, x:int, y:int, z:int) -> bool:
        for side in sides:
            nx, ny, nz = x, y, z
            while True:
                nx += side[0]
                ny += side[1]
                nz += side[2]
                if (nx, ny, nz) in cubes:
                    break
                if abs(nx) > 100 or abs(ny) > 100 or abs(nz) > 100:
                    return True

        return False

    def PartA(self):
        self.StartPartA()

        cubes = {}
        for line in self.inputdata:
            x, y, z = line.strip().split(",")
            x, y, z = int(x), int(y), int(z)
            cubes[(x, y, z)] = True

        answer = 0

        for k in cubes.keys():
            answer += self.sides_occupied(cubes, k[0], k[1], k[2])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        maxx = maxy = maxz = -1_000_000
        minx = miny = minz = 1_000_000
        cubes = {}
        for line in self.inputdata:
            x, y, z = line.strip().split(",")
            x, y, z = int(x), int(y), int(z)
            cubes[(x, y, z)] = True
            maxx = max(x, maxx)
            maxy = max(y, maxy)
            maxz = max(z, maxz)
            minx = min(x, minx)
            miny = min(y, miny)
            minz = min(z, minz)

        print(f"X: {minx}-{maxx} Y: {miny}-{maxy} Z: {minz}-{maxz} ")

        answer = 0

        for k in cubes.keys():
            answer += self.sides_occupied(cubes, k[0], k[1], k[2])

        for x in range(minx + 1, maxx ):
            for y in range(miny + 1, maxy ):
                for z in range(minz + 1, maxz):
                    if (x, y, z) not in cubes:
                        if not self.open_to_air(cubes, x, y, z):
                            # print(f"Enclosed: {x}, {y}, {z}")
                            answer -= self.sides_occupied_2(cubes, x, y, z)

        for z in range(maxz + 1):
            print(f"*** 2: {z} ****************")
            for y in range(maxy + 1):
                for x in range(maxx + 1):
                    print("#" if (x,y,z) in cubes else ".", end="")
                print("")
            a = input()

        # Attempt 1: 1364 is too low
        # Attempt 2: 2029 is too low

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day18Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

