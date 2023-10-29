from .punkt import Punkt


class NazwanyPunkt(Punkt):
    __slots__ = ['nazwa']

    def __init__(self, x: float, y: float, nazwa: str) -> None:
        super().__init__(x, y)
        self.nazwa = nazwa

    def __str__(self) -> str:
        return f'{self.nazwa}: ({self.x}, {self.y})'

    def __del__(self) -> None:
        self.nazwa = ""
