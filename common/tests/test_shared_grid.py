import pytest
from common.grid import Grid

def test_Grid_constructor():
    grid = Grid()
    assert grid.elements is None

def test_Grid_initialize_from_strings():
    # 3x3 grid of '.' characters.
    character = '.'
    strings = [character * 3] * 3
    grid = Grid()
    grid.initialize_from_strings(strings)
    assert len(grid.elements) == len(strings)
    assert len(grid.elements[0]) == len(strings[0])
    assert grid.elements[0][0] == character

def test_Grid_str():
    # 3x3 grid of '.' characters.
    character = '.'
    strings = [character * 3] * 3
    grid = Grid()
    grid.initialize_from_strings(strings)
    assert str(grid) == '\n'.join(['.' * 3] * 3)

@pytest.mark.parametrize("strings,pattern,expected", [
    (
        [
            '.1.2.3.',
            '4.5.6.7',
            '.8.9.0.'
        ],
        r"\d",
        [
            {'row':0, 'start':1, 'end':1, 'value':'1'}, 
            {'row':0, 'start':3, 'end':3, 'value':'2'}, 
            {'row':0, 'start':5, 'end':5, 'value':'3'}, 
            {'row':1, 'start':0, 'end':0, 'value':'4'}, 
            {'row':1, 'start':2, 'end':2, 'value':'5'}, 
            {'row':1, 'start':4, 'end':4, 'value':'6'}, 
            {'row':1, 'start':6, 'end':6, 'value':'7'}, 
            {'row':2, 'start':1, 'end':1, 'value':'8'}, 
            {'row':2, 'start':3, 'end':3, 'value':'9'}, 
            {'row':2, 'start':5, 'end':5, 'value':'0'} 
        ]
    ),
    (
        [
            '1.21.321'
        ],
        r"(\d+)",
        [
            {'row':0, 'start':0, 'end':0, 'value':'1'}, 
            {'row':0, 'start':2, 'end':3, 'value':'21'}, 
            {'row':0, 'start':5, 'end':7, 'value':'321'},
        ]
    )
])
def test_Grid_find_tokens_in_rows(strings,pattern,expected):
    grid = Grid()
    grid.initialize_from_strings(strings)
    tokens = [x for x in grid.find_tokens_in_rows(pattern)]
    assert tokens == expected

@pytest.mark.parametrize("row,start,end,expected", [
    (0,0,0,['2','4','5']),
    (0,1,1,['1','3','4','5','6']),
    (0,2,2,['2','5','6']),
    (1,0,0,['1','2','5','7','8']),
    (1,1,1,['1','2','3','4','6','7','8','9']),
    (1,2,2,['2','3','5','8','9']),
    (2,0,0,['4','5','8']),
    (2,1,1,['4','5','6','7','9']),
    (2,2,2,['5','6','8']),
])
def test_Grid_get_surrounding_elements(row : int, start : int, end : int, expected):
    strings = [
        '123',
        '456',
        '789'
    ]
    grid = Grid()
    grid.initialize_from_strings(strings)
    surrounding_elements = [x['value'] for x in grid.get_surrounding_elements(row, start, end)]
    assert surrounding_elements == expected