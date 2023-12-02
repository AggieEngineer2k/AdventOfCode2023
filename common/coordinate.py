class Coordinate:
    _x : float
    _y : float
    def __init__(self, x : float = 0, y : float = 0):
        self._x = float(x)
        self._y = float(y)
    def get_tuple(self) -> "tuple[float, float]":
        return (self._x, self._y)
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Coordinate):
            return self._x == other._x and self._y == other._y
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(self.get_tuple())
    @property
    def x(self) -> float:
      return self._x
    @property
    def y(self) -> float:
      return self._y