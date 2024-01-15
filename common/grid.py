import re

class Grid:
    def __init__(self):
        self.elements = None
        self.height = None
        self.width = None

    def initialize_from_strings(self, strings : "list(str)"):
        self.elements = [[x for x in y] for y in strings]
        self.update_grid_dimensions()

    def update_grid_dimensions(self):
        self.height = len(self.elements)
        self.width = len(self.elements[0])

    def find_tokens_in_rows(self, pattern : str):
        "Returns a tuple with the row index, element index, and matching value for each matching pattern."
        for row_index in range(len(self.elements)):
            row = ''.join(self.elements[row_index])
            for m in re.finditer(pattern, row):
                #yield (row_index, m.start(0), m.group(0))
                yield {
                    "row": row_index,
                    "start": m.start(0),
                    "end": m.start(0) + len(m.group(0)) - 1,
                    "value": m.group(0)
                }

    def get_row(self, row : int):
        return self.elements[row]
    
    def get_column(self, column : int):
        return [self.elements[x][column] for x in range(self.height)]
    
    def replace_row(self, row : int, elements):
        if len(self.get_row(row)) != len(elements):
            raise Exception('Cardinality mismatch between row and replacements.')
        self.elements[row] = elements
        
    def replace_column(self, column : int, elements):
        if len(self.get_column(column)) != len(elements):
            raise Exception('Cardinality mismatch between column and replacements.')
        for i in range(len(elements)):
            self.elements[i][column] = elements[i]

    def get_element(self, row : int, column : int):
        return {
            "row": row,
            "column": column,
            "value" : self.elements[row][column]
        }

    def get_surrounding_elements(self, row : int, start : int, end : int):
        "Returns the elements surrounding the elements on a row from the start to end indices."
        # Inspect the elements above.
        if row > 0:
            #for x in self.elements[row - 1][max(0,start - 1):min(len(self.elements[row]) - 1, end + 1) + 1]:
            for column in range(max(0,start - 1), min(len(self.elements[row]) - 1, end + 1) + 1):
                yield self.get_element(row - 1, column)
        # Inspect the element to the left.
        if start > 0:
            yield self.get_element(row,start - 1)
        # Inspect the element to the right.
        if end < len(self.elements[row]) - 1:
            yield self.get_element(row,end + 1)
        # Inspect the elements below.
        if row < len(self.elements) - 1:
            #for x in self.elements[row + 1][max(0,start - 1):min(len(self.elements[row]) - 1, end + 1) + 1]:
            for column in range(max(0,start - 1), min(len(self.elements[row]) - 1, end + 1) + 1):
                yield self.get_element(row + 1, column)

    def insert_row(self, row : int, element):
        row_to_insert = [element] * self.width
        self.elements.insert(row, row_to_insert)
        self.update_grid_dimensions()

    def insert_column(self, column : int, element):
        for x in range(self.height):
            self.elements[x].insert(column, element)
        self.update_grid_dimensions()

    def remove_row(self, row : int):
        del self.elements[row]
        self.update_grid_dimensions()

    def remove_column(self, column : int):
        for x in range(self.height):
            del self.elements[x][column]
        self.update_grid_dimensions()

    def __str__(self):
        return '\n'.join([''.join([str(element) for element in row]) for row in self.elements])
    
    def set_value(self, row : int, column : int, value):
        self.elements[row][column] = value