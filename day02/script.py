# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
import re
from common.input_parser import InputParser

# Define the puzzle solver.
class Solver:
    input : "list(str)"
   
    def __init__(self, input : str = []):
        self.input = input

    # Returns what you learn about a game.
    # Namely, its Id and the greatest numbers of each colored cubes seen at one time.
    def learn(self, game : str) -> "dict":
        learned = {
            "id" : 0,
            "red": 0,
            "green": 0,
            "blue": 0
        }
        # Extract the game Id.
        learned["id"] = int(re.match(r"Game (\d+):",game)[1])
        # Tabulate the highest number of cubes of each color seen in a handful.
        for reveal in re.findall(r"(\d+) (\w+)",game):
            learned[reveal[1]] = max(learned[reveal[1]], int(reveal[0]))
        return learned
    
    # Returns whether a game is possible with the given cube constraints based on what was learned.
    # That is, what we've learned cannot exceed the cube limits.
    def possible(self, learned : dict) -> bool:
        return learned["red"] <= 12 and learned["green"] <= 13 and learned["blue"] <= 14
    
    # Calculates the power of a game based on what was learned.
    def power(self, learned : dict) -> int:
        return learned["red"] * learned["green"] * learned["blue"]

    def day_1(self):
        learnings = [self.learn(game) for game in self.input]
        result = sum([learning["id"] if self.possible(learning) else 0 for learning in learnings])
        print(f"Day 1: {result}")

    def day_2(self):
        learnings = [self.learn(game) for game in self.input]
        result = sum([self.power(learning) for learning in learnings])
        print(f"Day 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.day_1()
solver.day_2()