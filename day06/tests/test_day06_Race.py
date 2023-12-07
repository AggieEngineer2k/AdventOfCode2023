import pytest
from day06.script import Race

@pytest.mark.parametrize('time,distance,expected', [
    (7,9,[
        (0,0),
        (1,6),
        (2,10),
        (3,12),
        (4,12),
        (5,10),
        (6,6),
        (7,0)
    ]),
])
def test_Race_get_options(time : int, distance : int, expected : "list(tuple)"):
    race = Race(time,distance)
    actual = [x for x in race.get_options()]
    assert actual == expected

@pytest.mark.parametrize('time,distance,expected', [
    (7,9,[
        (2,10),
        (3,12),
        (4,12),
        (5,10),
    ]),
])
def test_Race_get_winning_options(time : int, distance : int, expected : "list(tuple)"):
    race = Race(time,distance)
    actual = [x for x in race.get_winning_options()]
    assert actual == expected