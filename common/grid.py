import re

class Grid:
    def __init__(self):
        self.elements = None

    def initialize_from_strings(self, strings : "list(str)"):
        self.elements = [[x for x in y] for y in strings]

    def find_tokens_in_rows(self, pattern : str):
        "Returns a tuple with the row index, element index, and matching value for each matching pattern."
        for row_index in range(len(self.elements)):
            row = ''.join(self.elements[row_index])
            for m in re.finditer(pattern, row):
                yield (row_index, m.start(0), m.group(0))

    def get_surrounding_elements(self, row : int, start : int, end : int):
        # Inspect the elements above.
        if row > 0:
            for x in self.elements[row - 1][max(0,start - 1):min(len(self.elements[row]) - 1, end + 1) + 1]:
                yield x
        # Inspect the element to the left.
        if start > 0:
            yield self.elements[row][start - 1]
        # Inspect the element to the right.
        if end < len(self.elements[row]) - 1:
            yield self.elements[row][end + 1]
        # Inspect the elements below.
        if row < len(self.elements) - 1:
            for x in self.elements[row + 1][max(0,start - 1):min(len(self.elements[row]) - 1, end + 1) + 1]:
                yield x