from aoc import Aoc
import itertools
import math
import re
import sys

# Day 7
# https://adventofcode.com/2022

class Folder():
    def __init__(self, name:str):
        self.name = name
        self.files = []  # [(name, size), ...]
        self.folders = []
        self.parent = None

    def total_file_size(self):
        return sum([f[1] for f in self.files])
    
    def total_size(self):
        return sum([ f.total_size() for f in self.folders ]) + self.total_file_size()

    def total_size_parta(self, maximum:int):
        # return sum([ f.total_size() for f in self.folders if f.total_size() <= maximum ])# + self.total_file_size()
        s = sum([ f.total_size() for f in self.folders ]) + self.total_file_size()
        return s if s < maximum else 0

    def add_folder(self, name:str) -> None:
        f = Folder(name)
        f.parent = self
        self.folders.append(f)
    
    def add_file(self, name:str, size:int) -> None:
        self.files.append((name, size))
    
    def up_dir(self):
        return self.parent

    def cd_dir(self, name:str):
        for f in self.folders:
            if f.name == name:
                return f
        print(f"CD in unknown folder {name}")
        return None 

class Day7Solution(Aoc):

    def Run(self):
        self.StartDay(7, "No Space Left On Device")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(7)

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
        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 95437

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

    def count_part_a(self, folder):
        for f in folder.folders:
            if f.total_size() < 100_000:
                self.parta_size += f.total_size()
            self.count_part_a(f)

    def PartA(self):
        self.StartPartA()

        root = Folder("/")
        current = root

        for line in self.inputdata:
            m = re.match(r"\$ cd (.*)", line)
            if m:
                name = m.group(1)
                # print(f"CD {name}")
                if name == "/":
                    current = root
                elif name == "..":
                    current = current.up_dir()
                else:
                    current = current.cd_dir(name)

            m = re.match(r"\$ ls", line)
            if m:
                #print("LS")
                pass

            m = re.match(r"dir (.*)", line)
            if m:
                name = m.group(1)
                current.add_folder(name)

            m = re.match(r"(\d*) (.*)", line)
            if m:
                size = int(m.group(1))
                name = m.group(2)
                current.add_file(name, size)

        self.parta_size = 0
        self.count_part_a(root)
        answer = self.parta_size

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day7Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

