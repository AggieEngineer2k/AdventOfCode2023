import pytest
from day03.script import Solver

@pytest.mark.parametrize('schematic,expected', [
    ([
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ],[467,35,633,617,592,755,664,598]),
    # Test literal edge cases.
    ([
        "123....321",
        "*456..654*",
        "789....987",
        "000....999"
    ],[123,321,456,654,789,987]),
    # Test repeated numbers.
    ([
        "321.321.321",
        ".*.......*.",
        "123.123.123"
    ],[321,321,123,123]),
])
def test_extractPartNumbers(schematic : "list(str)", expected : "list(int)"):
    solver = Solver()
    actual = solver.extractPartNumbers(schematic)
    assert actual == expected