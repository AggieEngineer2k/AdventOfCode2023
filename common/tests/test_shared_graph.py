import pytest
from common.graph import Graph

def test_Graph_constructor():
    graph = Graph()
    assert graph.dictionary == {}

def test_Graph_add_edge_to_graph():
    graph = Graph()
    graph.add_edge("London","Dublin",464)
    assert graph.dictionary == {"London":{"Dublin":464},"Dublin":{"London":464}}
    graph.add_edge("London","Belfast",518)
    assert graph.dictionary == {"London":{"Dublin":464,"Belfast":518},"Dublin":{"London":464},"Belfast":{"London":518}}
    graph.add_edge("Belfast","Dublin",141)
    assert graph.dictionary == {"London":{"Dublin":464,"Belfast":518},"Dublin":{"London":464,"Belfast":141},"Belfast":{"London":518,"Dublin":141}}

# Given the following distances:
#     London to Dublin = 464
#     London to Belfast = 518
#     Dublin to Belfast = 141
# The possible routes are therefore:
#     Dublin -> London -> Belfast = 982
#     London -> Dublin -> Belfast = 605
#     London -> Belfast -> Dublin = 659
#     Dublin -> Belfast -> London = 659
#     Belfast -> Dublin -> London = 605
#     Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605.

def test_Graph_get_traveling_salesman_shortest():
    graph = Graph()
    graph.add_edge("London","Dublin",464)
    graph.add_edge("London","Belfast",518)
    graph.add_edge("Belfast","Dublin",141)
    traveling_salesman = graph.get_traveling_salesman_shortest()
    assert traveling_salesman[0] == 605
    assert traveling_salesman[1] == ["London","Dublin","Belfast"]

# Given the distances above, the longest route would be 982 via Dublin -> London -> Belfast.

def test_Graph_get_traveling_salesman_longest():
    graph = Graph()
    graph.add_edge("London","Dublin",464)
    graph.add_edge("London","Belfast",518)
    graph.add_edge("Belfast","Dublin",141)
    traveling_salesman = graph.get_traveling_salesman_longest()
    assert traveling_salesman[0] == 982
    assert traveling_salesman[1] == ["Dublin","London","Belfast"]