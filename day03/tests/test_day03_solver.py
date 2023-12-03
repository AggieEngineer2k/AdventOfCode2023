import pytest
from day03.script import Solver

# @pytest.mark.parametrize('learned,expected', [
#     ({
#         "id": 1,
#         "red": 4,
#         "green": 2,
#         "blue": 6
#     },48),
#     ({
#         "id": 2,
#         "red": 1,
#         "green": 3,
#         "blue": 4
#     },12),
#     ({
#         "id": 3,
#         "red": 20,
#         "green": 13,
#         "blue": 6
#     },1560),
#     ({
#         "id": 4,
#         "red": 14,
#         "green": 3,
#         "blue": 15
#     },630),
#     ({
#         "id": 5,
#         "red": 6,
#         "green": 3,
#         "blue": 2
#     },36)
# ])
# def test_solver_power(learned : dict, expected : int):
#     solver = Solver()
#     actual = solver.power(learned)
#     assert actual == expected