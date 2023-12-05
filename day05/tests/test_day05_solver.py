import pytest
from day05.script import Solver

input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def test_Solver_parse_input():
    solver = Solver()
    solver.parse_input(input.split('\n'))
    assert solver.parsed_input['seeds'] == [79,14,55,13]
    assert solver.parsed_input['seed-to-soil'].mappings == [
        {'destination': 50, 'source': 98, 'range': 2},
        {'destination': 52, 'source': 50, 'range': 48}
    ]

@pytest.mark.parametrize('seed,expected', [
    (79,82),
    (14,43),
    (55,86),
    (13,35)
])
def test_Solver_get_location_for_seed(seed : int, expected : int):
    solver = Solver()
    solver.parse_input(input.split('\n'))
    actual = solver.get_location_for_seed(seed)
    assert actual == expected