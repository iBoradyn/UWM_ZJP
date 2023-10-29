class Punkt:
    __slots__ = ['__dict__', '_x', '_y']

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @x.deleter
    def x(self):
        del self._x

    @y.deleter
    def y(self):
        del self._y

    def __str__(self) -> str:
        return f'<{self.x}, {self.y}>'

    def __repr__(self) -> str:
        return str(self)

    def move(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y
