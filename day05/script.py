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
    def get_source(self, destination : int) -> int:
        for mapping in self.mappings:
            # Isolate a mapping that covers the desitnation number.
            if (mapping['destination'] <= destination) and (mapping['destination'] + mapping['range'] > destination):
                return mapping['source'] + (destination - mapping['destination'])
        # Return the destination number when no covering mapping is found.
        return destination

# Define the puzzle solver.
class Solver:
    mapping_names = None

    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)" = None):
        self.mapping_names = []
        result = {}
        for line in input or self.input:
            if re.match('seeds:', line):
                result['seeds'] = [int(x) for x in re.findall(r'(\d+)', line)]
            elif re.match(r'([a-z-]+) map:', line):
                mapping_name = line[:-5]
                current_mapping = result[mapping_name] = ThingToThingMap()
                self.mapping_names.append(mapping_name)
            elif re.match(r'(\d+) (\d+) (\d+)', line):
                current_mapping.add_mapping(line)
        self.parsed_input = result
        return result
    
    def get_location_for_seed(self, seed : int, parsed_input : dict = None) -> int:
        parsed = parsed_input or self.parsed_input
        result = seed
        for x in self.mapping_names:
            result = parsed[x].get_destination(result)
        return result
    
    def get_seed_for_location(self, location : int, parsed_input : dict = None) -> int:
        parsed = parsed_input or self.parsed_input
        result = location
        for x in [x for x in reversed(self.mapping_names)]:
            result = parsed[x].get_source(result)
        return result

    def part_1(self):
        result = min([self.get_location_for_seed(x) for x in self.parsed_input['seeds']])
        print(f"Part 1: {result}")

    def part_2(self):
        seeds = list(zip(self.parsed_input['seeds'][0::2],self.parsed_input['seeds'][1::2]))
        humidity_to_location_mapping = self.parsed_input['humidity-to-location'].mappings.copy()
        humidity_to_location_mapping.sort(key=lambda x: x['destination'])
        result = None
        # ---
        # Attempt 2: Walk through mappings to bracketize splits.
        # ---
        sources = [x[0] for x in seeds]
        destinations = []
        for mapping_name in self.mapping_names:
            for source in sources:
                destination = self.parsed_input[mapping_name].get_destination(source)
                destinations.append(destination)
            sources = destinations.copy()
            destinations = []
        sources.sort()
        logging.debug(sources)
        result = self.get_seed_for_location(sources[0])
        
        # ---
        # Attempt 1: Brute force through locations to find the first that maps back to a seed.
        # ---
        # for humidity_to_location in humidity_to_location_mapping:
        #     for x in range(humidity_to_location['destination'],humidity_to_location['destination'] + humidity_to_location['range']):
        #         seed = self.get_seed_for_location(x)
        #         for seed_bucket in seeds:
        #             if (seed_bucket[0] <= seed) and (seed_bucket[0] + seed_bucket[1] > seed):
        #                 logging.debug(f"Seed for location {x} is {seed} in seed range ({seed_bucket[0],seed_bucket[1]}).")
        #                 result = seed
        #             break
        #         if result is not None:
        #             break
        #     if result is not None:
        #         break
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
solver.parse_input()
# Solve the puzzles.
solver.part_1()
solver.part_2()