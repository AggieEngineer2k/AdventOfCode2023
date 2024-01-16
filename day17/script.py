# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.WARNING)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
from enum import Enum

class Path(Enum):
    START = 'S'
    BLANK = '.'
    UP = '^'
    DOWN = 'V'
    LEFT = '<'
    RIGHT = '>'
    END = 'E'

# Implementation of Dijkstra's algorithm for finding the shortest paths between nodes in a weighted graph.
class ShortestPathVertex:
    def __init__(self, row : int, column : int, heat_loss : float):
        self.visited = False
        self.total_heat_loss = float('inf')
        self.row = row
        self.column = column
        self.heat_loss = heat_loss
        self.path = Path.BLANK
        # Reference to the previous vertex in the shortest path.
        self.parent : ShortestPathVertex = None
        self.previous_direction = Path.BLANK
        self.previous_blocks = 0
    def __str__(self) -> str:
        return self.path.value

class ShortestPathGraph:
    def __init__(self, vertices):
        # Create the graph of vertices.
        self.vertices = [[ShortestPathVertex(r,c,vertices[r][c]) for c in range(len(vertices[r]))] for r in range(len(vertices))]
        # Inspect the dimensions of the graph.
        self.rows = len(self.vertices)
        self.columns = len(self.vertices[0])
        # Create a set for storing the vertices in the shortest path.
        self.shortest_path_tree = set()
    def findUnvisitedNeighbors(self, current : ShortestPathVertex, previous_direction : Path, previous_blocks : int) -> "list[ShortestPathVertex]":
        neighbors : list[ShortestPathVertex] = []
        # Up
        if current.row > 0 and not (previous_direction == Path.UP and previous_blocks == 3):
            neighbors.append(self.vertices[current.row - 1][current.column])
        # Down
        if current.row < self.rows - 1 and not (previous_direction == Path.DOWN and previous_blocks == 3):
            neighbors.append(self.vertices[current.row + 1][current.column])
        # Left
        if current.column > 0 and not (previous_direction == Path.LEFT and previous_blocks == 3):
            neighbors.append(self.vertices[current.row][current.column - 1])
        # Right
        if current.column < self.columns - 1 and not (previous_direction == Path.RIGHT and previous_blocks == 3):
            neighbors.append(self.vertices[current.row][current.column + 1])
        results = [neighbor for neighbor in neighbors if not neighbor.visited]
        logging.debug(f"Unvisited neighbors for ({current.row},{current.column}) are: {', '.join([f'({x.row},{x.column})' for x in results])}.")
        return results
    def findUnvisitedVertexWithSmallestTotalHeatLoss(self):
        unvisited = [vertex for _, row in enumerate(self.vertices) for _, vertex in enumerate(row) if vertex.visited == False]
        unvisited.sort(key=lambda x: x.total_heat_loss)
        logging.debug(f'Next to visit is ({unvisited[0].row},{unvisited[0].column}) {unvisited[0].path.value} from ({unvisited[0].parent.row},{unvisited[0].parent.column}).')
        return unvisited[0]
    def findShortestPath(self, start : ShortestPathVertex, end : ShortestPathVertex):
        start.total_heat_loss = 0
        start.path = Path.START
        end.path = Path.END
        # Start searching from the starting vertex and continue searching until the ending vertex is the next to be visited.
        current = start
        while current != end:
            logging.debug(f'Visiting ({current.row},{current.column}) at total heat loss {current.total_heat_loss} after {current.previous_blocks} {current.previous_direction.value}.')
            for neighbor in self.findUnvisitedNeighbors(current, current.previous_direction, current.previous_blocks):
                if neighbor.total_heat_loss > current.total_heat_loss + neighbor.heat_loss:
                    neighbor.total_heat_loss = current.total_heat_loss + neighbor.heat_loss
                    neighbor.parent = current
                    if(neighbor.row < current.row):
                        neighbor.path = Path.UP
                    elif(neighbor.row > current.row):
                        neighbor.path = Path.DOWN
                    elif(neighbor.column > current.column):
                        neighbor.path = Path.RIGHT
                    elif(neighbor.column < current.column):
                        neighbor.path = Path.LEFT
                    # Keep track of the direction and blocks traveled.
                    neighbor.previous_direction = neighbor.path
                    if(current.previous_direction == neighbor.path):
                        neighbor.previous_blocks = current.previous_blocks + 1
                    else:
                        neighbor.previous_blocks = 1
            current.visited = True
            current = self.findUnvisitedVertexWithSmallestTotalHeatLoss()
        current.path = Path.END
        return end
    def __str__(self) -> str:
        return '\n'.join([''.join([str(c) for c in r]) for r in self.vertices])

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
graph = ShortestPathGraph([[float(x) for x in list(line)] for line in input])
# Top left to bottom right.
start = graph.vertices[0][0]
end = graph.vertices[graph.rows - 1][graph.columns - 1]
graph.findShortestPath(start,end)
logging.debug('GRAPH:\n' + str(graph))
print(f"Part 1: {end.total_heat_loss}")