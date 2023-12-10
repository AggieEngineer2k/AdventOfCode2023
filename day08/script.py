# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re
from common.math import lcm

L = 'L'
R = 'R'

# Define the puzzle solver.
class Solver:
    directions : str
    nodes = {}

    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)" = None):
        self.nodes.clear()
        input_to_parse = input or self.input
        for line in input_to_parse:
            match_direction = re.match(r"^[RL]+$", line)
            match_path = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
            if match_direction:
                self.directions = line
            elif match_path:
                self.nodes[match_path.group(1)] = {
                    L: match_path.group(2),
                    R: match_path.group(3)
                }
    
    def part_1(self):
        direction_index = 0
        steps = 0
        current_node = "AAA"
        while current_node != "ZZZ":
            current_node = self.nodes[current_node][self.directions[direction_index]]
            direction_index += 1
            if direction_index == len(self.directions):
                direction_index = 0
            steps += 1
        result = steps
        print(f"Part 1: {result}")

    def part_2(self):
        ghost_nodes = [x for x in self.nodes.keys() if x[-1]=='A']
        steps = [0] * len(ghost_nodes)
        for i in range(len(ghost_nodes)):
            direction_index = 0
            while ghost_nodes[i][-1] != 'Z':
                ghost_nodes[i] = self.nodes[ghost_nodes[i]][self.directions[direction_index]]
                direction_index += 1
                if direction_index == len(self.directions):
                    direction_index = 0
                steps[i] += 1
        result = lcm(steps)
        
        # ---
        # Attempt 1: Brute Force
        # ---
        # direction_index = 0
        # steps = 0
        # current_nodes = [x for x in self.nodes.keys() if x[-1]=='A']
        # while not all(x[-1]=='Z' for x in current_nodes):
        #     logging.debug(f"Step {steps} {current_nodes}.")
        #     for i in range(len(current_nodes)):
        #         current_nodes[i] = self.nodes[current_nodes[i]][self.directions[direction_index]]
        #     direction_index += 1
        #     if direction_index == len(self.directions):
        #         direction_index = 0
        #     steps += 1
        
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
solver.parse_input()
# Solve the puzzles.
solver.part_1()
solver.part_2()