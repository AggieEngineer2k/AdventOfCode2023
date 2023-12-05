# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re

# Assumption: Constructing complete source-destination collections through brute force will not scale.
class ThingToThingMap:
    mappings : "list"
    def __init__(self, mappings : list = None):
        self.mappings = mappings or []
    # def sort_mappings(self):
    #     self.mappings.sort(key=lambda x: x['source'])
    def add_mapping(self, mapping : str):
        tokens = re.findall(r'(\d+)', mapping)
        self.mappings.append({
            'destination': int(tokens[0]),
            'source': int(tokens[1]),
            'range': int(tokens[2])
        })
        #self.sort_mappings()
    def get_destination(self, source : int) -> int:
        for mapping in self.mappings:
            # Isolate a mapping that covers the source number.
            if (mapping['source'] <= source) and (mapping['source'] + mapping['range'] > source):
                return mapping['destination'] + (source - mapping['source'])
        # Return the source number when no covering mapping is found.
        return source

# Define the puzzle solver.
class Solver:
    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)"):
        result = {}
        for line in input:
            if re.match('seeds:', line):
                result['seeds'] = [int(x) for x in re.findall(r'(\d+)', line)]
            elif re.match(r'([a-z-]+) map:', line):
                current_mapping = result[line[:-5]] = ThingToThingMap()
            elif re.match(r'(\d+) (\d+) (\d+)', line):
                current_mapping.add_mapping(line)
        self.parsed_input = result
        return result
    
    def get_location_for_seed(self, seed : int, parsed_input : dict = None) -> int:
        parsed = parsed_input or self.parsed_input
        result = seed
        for x in [
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            'light-to-temperature',
            'temperature-to-humidity',
            'humidity-to-location'
        ]:
            result = parsed[x].get_destination(result)
        return result

    def part_1(self):
        result = None
        print(f"Part 1: {result}")

    def part_2(self):
        result = None
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()