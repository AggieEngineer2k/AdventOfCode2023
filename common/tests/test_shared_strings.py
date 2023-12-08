import pytest
from common.strings import all_replacements

@pytest.mark.parametrize("s,w,r,expected", [
    (
        'a*c',
        '*',
        ['x','y','z'],
        ['axc','ayc','azc']
    ),
    (
        'a*b*c',
        '*',
        ['x','y','z'],
        ['axbxc','axbyc','axbzc','aybxc','aybyc','aybzc','azbxc','azbyc','azbzc']
    ),
    (
        'a*c',
        '*',
        ['b','*'],
        ['abc']
    ),
    (
        'abc',
        '*',
        ['z'],
        ['abc']
    ),
    (
        'a*',
        '*',
        ['b','c'],
        ['ab','ac']
    ),
])
def test_all_replacements(s,w,r,expected):
    actual = [*all_replacements(s,w,r)]
    assert actual == expected