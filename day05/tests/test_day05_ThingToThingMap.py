import pytest
from day05.script import ThingToThingMap

mapping = [
    {'destination': 50, 'source': 98, 'range': 2},
    {'destination': 52, 'source': 50, 'range': 48}
]
@pytest.mark.parametrize('mapping,source,expected', [
    (mapping,0,0),
    (mapping,1,1),
    (mapping,48,48),
    (mapping,49,49),
    (mapping,50,52),
    (mapping,51,53),
    (mapping,96,98),
    (mapping,97,99),
    (mapping,98,50),
    (mapping,99,51),
    (mapping,79,81),
    (mapping,14,14),
    (mapping,55,57),
    (mapping,13,13),
])
def test_ThingToThingMap_get_destination(mapping : list, source : int, expected : int):
    thingToThingMap = ThingToThingMap(mapping)
    actual = thingToThingMap.get_destination(source)
    assert actual == expected