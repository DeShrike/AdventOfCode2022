from aoc import Aoc
import random
import itertools
import math
import re
import sys

# Day 19
# https://adventofcode.com/2022

class Blueprint():
    def __init__(self, id: int, ore_robot_ore: int, clay_robot_ore: int, obsidian_robot_ore: int, obsidian_robot_clay: int, geode_robot_ore: int, geode_robot_obsidian: int):
        self.id = id
        self.ore_robot_ore = ore_robot_ore
        self.clay_robot_ore = clay_robot_ore
        self.obsidian_robot_ore = obsidian_robot_ore
        self.obsidian_robot_clay = obsidian_robot_clay
        self.geode_robot_ore = geode_robot_ore
        self.geode_robot_obsidian = geode_robot_obsidian

    def evaluate(self, chromosome) -> int:
        if len(chromosome) != 24:
            print("error")
        orerobots = 1
        clayrobots = 0
        obsideanrobots = 0
        geoderobots = 0
        clay = 0
        ore = 0
        geodes = 0
        obsidian = 0
        for gene in chromosome:
            new_geode_robot = 0
            new_obsidian_robot = 0
            new_clay_robot = 0
            new_ore_robot = 0

            if gene == "W":
                ore += orerobots
                clay += clayrobots
                obsidian += obsideanrobots
                geodes += geoderobots
            elif gene == "O":
                if ore >= self.ore_robot_ore:
                    # print("create ore robot")
                    new_ore_robot = 1
                    ore -= self.ore_robot_ore
                else:
                    return 0
                ore += orerobots
                clay += clayrobots
                obsidian += obsideanrobots
                geodes += geoderobots

                orerobots += new_ore_robot
            elif gene == "C":
                if ore >= self.clay_robot_ore:
                    # print("create clay robot")
                    new_clay_robot = 1
                    ore -= self.clay_robot_ore
                else:
                    return 0
                ore += orerobots
                clay += clayrobots
                obsidian += obsideanrobots
                geodes += geoderobots

                clayrobots += new_clay_robot
            elif gene == "B":
                if ore >= self.obsidian_robot_ore and clay >= self.obsidian_robot_clay:
                    # print("create obsidian robot")
                    new_obsidian_robot = 1
                    ore -= self.obsidian_robot_ore
                    clay -= self.obsidian_robot_clay
                else:
                    return 0
                ore += orerobots
                clay += clayrobots
                obsidian += obsideanrobots
                geodes += geoderobots

                obsideanrobots += new_obsidian_robot
            elif gene == "G":
                if ore >= self.geode_robot_ore and obsidian >= self.geode_robot_obsidian:
                    # print("create geode robot")
                    new_geode_robot = 1
                    ore -= self.geode_robot_ore
                    obsidian -= self.geode_robot_obsidian
                else:
                    return 0
                ore += orerobots
                clay += clayrobots
                obsidian += obsideanrobots
                geodes += geoderobots

                geoderobots += new_geode_robot

        return geodes


class GA():
    def __init__(self, minutes: int, bp: Blueprint):
        self.minutes = minutes
        self.blueprint = bp
        self.genes = [ "W", "G", "O", "B", "C" ]
        self.pop_count = 50
        self.population = [self.create_chromosome() for _ in range(self.pop_count)]
        self.generations = 10000

    def create_chromosome(self):
        c = [ random.choice(self.genes) for _ in range(self.minutes)]
        c[0] = "W"
        c[1] = "W"
        c[2] = "W"
        c[3] = "O"
        return c

    def selection(self):
        pass

    def mutate(self):
        for _ in range(3):
            c = self.population[random.randint(0, len(self.population) - 1)]
            c = c[:]
            gene_ix = random.randint(0, self.minutes - 1)
            c[gene_ix] = random.choice(self.genes)

    def crossover(self):
        pass

    def next_generation(self):
        scores = [(self.blueprint.evaluate(chromosome), chromosome) for chromosome in self.population]
        scores.sort(key=lambda i: i[0], reverse=True)
        scores = [score for score in scores if score[0] > 0]
        if len(scores) > 0:
            print("YES", len(scores), scores[0][0])

        self.population = [score[1] for score in scores]

        if len(self.population) > 0:
            self.mutate()

        while len(self.population) < self.pop_count:
            self.population.append(self.create_chromosome()) 

    def run(self):
        for _ in range(self.generations):
            self.next_generation()

class Day19Solution(Aoc):

    def Run(self):
        self.StartDay(19, "Not Enough Minerals")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(19)

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
        Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
        Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 33

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
        bps = []
        for line in self.inputdata:
            m = re.match(r"Blueprint (\d*): Each ore robot costs (\d*) ore. Each clay robot costs (\d*) ore. Each obsidian robot costs (\d*) ore and (\d*) clay. Each geode robot costs (\d*) ore and (\d*) obsidian.", line)
            if m:
                id = int(m.group(1))
                ore_robot_ore = int(m.group(2))
                clay_robot_ore = int(m.group(3))
                obsidian_robot_ore = int(m.group(4))
                obsidian_robot_clay = int(m.group(5))
                geode_robot_ore = int(m.group(6))
                geode_robot_obsidian = int(m.group(7))
                bps.append(Blueprint(id, ore_robot_ore, clay_robot_ore, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obsidian))

        return bps

    def find_quality_level(self, bp: Blueprint) -> int:
        minutes = 24
        ga = GA(minutes, bp)
        ga.run()
        return 0

    # def find_quality_level(self, bp: Blueprint) -> int:
    #     minutes = 24

    #     orerobots = 1
    #     clayrobots = 0
    #     obsideanrobots = 0
    #     geoderobots = 0
    #     clay = 0
    #     ore = 0
    #     geodes = 0
    #     obsidian = 0
    #     for minute in range(minutes):
    #         new_geoderobot = 0
    #         new_obsidian_robot = 0
    #         new_clay_robot = 0
    #         new_ore_robot = 0
    #         if obsidian >= bp.geode_robot_obsidian and ore >= bp.geode_robot_ore:
    #             print("Build geode robot")
    #             new_geoderobot = 1
    #             ore -= bp.geode_robot_ore
    #             obsidian -= bp.geode_robot_obsidian
    #         elif clay >= bp.obsidian_robot_clay and ore >= bp.obsidian_robot_ore and obsideanrobots == 0:
    #             print("Build obsidian robot")
    #             new_obsidian_robot = 1
    #             clay -= bp.obsidian_robot_clay
    #             ore -= bp.obsidian_robot_ore
    #         elif ore >= bp.clay_robot_ore and clayrobots == 0:
    #             print("Build clay robot")
    #             new_clay_robot = 1
    #             ore -= bp.clay_robot_ore
    #         elif ore >= bp.ore_robot_ore and orerobots < 2:
    #             print("Build ore robot")
    #             new_ore_robot = 1
    #             ore -= bp.ore_robot_ore

    #         ore += orerobots
    #         clay += clayrobots
    #         obsidian += obsideanrobots
    #         geodes += geoderobots

    #         geoderobots += new_geoderobot
    #         clayrobots += new_clay_robot
    #         orerobots += new_ore_robot
    #         obsideanrobots += new_obsidian_robot

    #         print(f"Minute {minute} : {ore} ore - {clay} clay - {obsidian} obsidian - {geodes} geodes")
    #         a = input()

    #     print(f"Bleuprint #{bp.id} : {geodes} geodes")
    #     return geodes * bp.id

    def PartA(self):
        self.StartPartA()

        blueprints = self.parse_input()

        answer = 0

        for bp in blueprints:
            ql = self.find_quality_level(bp)
            answer += ql

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day19Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

