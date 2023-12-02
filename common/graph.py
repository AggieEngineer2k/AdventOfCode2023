from itertools import permutations

# Undirected Weighted Graph
class Graph:
    def __init__(self):
        self.dictionary = {}
    
    def add_edge(self, from_node_name : str, to_node_name : str, weight : int, symmetric : bool = True):
        from_node_weights = self.dictionary.setdefault(from_node_name, {})
        from_node_weights.setdefault(to_node_name, weight)
        if (symmetric):
            to_node_weights = self.dictionary.setdefault(to_node_name, {})
            to_node_weights.setdefault(from_node_name, weight)

    def get_edge_weight(self, from_node_name : str, to_node_name : str) -> int:
        return self.dictionary[from_node_name][to_node_name]

    def get_traveling_salesman_shortest(self) -> tuple:
        node_names = list(self.dictionary.keys())
        shortest_path_weight = float("inf")
        shortest_path = None
        for permutation in [list(i) for i in permutations(node_names)]:
            weight = 0
            for step in [[permutation[i],permutation[i+1]] for i in range(len(permutation) - 1)]:
                weight += self.get_edge_weight(step[0],step[1])
            if weight < shortest_path_weight:
                shortest_path_weight = weight
                shortest_path = permutation
        return (shortest_path_weight, shortest_path)
    
    def get_traveling_salesman_longest(self) -> tuple:
        node_names = list(self.dictionary.keys())
        longest_path_weight = float("-inf")
        longest_path = None
        for permutation in [list(i) for i in permutations(node_names)]:
            weight = 0
            for step in [[permutation[i],permutation[i+1]] for i in range(len(permutation) - 1)]:
                weight += self.get_edge_weight(step[0],step[1])
            if weight > longest_path_weight:
                longest_path_weight = weight
                longest_path = permutation
        return (longest_path_weight, longest_path)
    
    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Graph):
            return self.dictionary == other.dictionary
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)