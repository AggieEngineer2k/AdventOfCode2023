import pytest
from common.coordinate import Coordinate

def test_Coordinate_constructor():
    coordinate = Coordinate()
    assert coordinate.x == 0
    assert coordinate.y == 0

@pytest.mark.parametrize("x,y,expected", [(0,0,(0,0)),(0,1,(0,1)),(1,0,(1,0)),(0,-1,(0,-1)),(-1,0,(-1,0))])
def test_Coordinate_get_tuple(x, y, expected):
    coordinate = Coordinate(x,y)
    actual = coordinate.get_tuple()
    assert actual == expected