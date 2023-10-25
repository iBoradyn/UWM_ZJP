import math
from pprint import pprint
from random import randint


class Square:
    """ Utworzyć klasę Square (kwadrat), która będzie zawierała inicjalizator ustawiający atrybut
    liczbowy side (długość boku), oraz metody:

    - area, która zwróci pole tego kwadratu
    - perimeter, która zwróci obwód tego kwadratu
    """
    side = 25

    def __init__(self, side=25):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4


class Triangle:
    """ Utworzyć klasę Triangle (trójkąt równoramienny), która będzie zawierała inicjalizator
    ustawiający atrybuty liczbowe:

    - side (długość boku)
    - height (wysokość),
    oraz metody:
    - area, która zwróci pole tego trójkąta
    - perimeter, która zwróci obwód tego trójkąta
    """
    side = 10
    height = 25

    def __init__(self, side=10, height=25):
        self.side = side
        self.height = height

    @property
    def __base(self):
        return math.sqrt(self.height**2 - self.side**2)*2

    def area(self):
        return (self.__base*self.height)/2

    def perimeter(self):
        return (self.side*2) + self.__base


""" Za pomocą pętli utworzyć listy:
- 10 kwadratów dla długości boków od 11 do 20
- 25 trójkątów dla długości boków od 6 do 10 i wysokości od 15 do 19
- Wyświetlić pola i obwody kazdej z tych figur
"""
squares_list = [Square(randint(11, 20)) for _ in range(10)]
triangles_list = [Triangle(randint(6, 10), randint(15, 19)) for _ in range(10)]

for i, square in enumerate(squares_list):
    print(f'Kwadrat {i+1}:')
    print(f'\t\tPole: {square.area()}')
    print(f'\t\tObwód: {square.perimeter()}')
for i, triangle in enumerate(triangles_list):
    print(f'Trójkąt {i+1}:')
    print(f'\t\tPole: {triangle.area()}')
    print(f'\t\tObwód: {triangle.perimeter()}')


class Tree:
    """Utworzyć klasę Tree (drzewo), która będzie zawierała inicjalizator ustawiający
    następujące atrybuty:

    - name (imię drzewa)
    - height (wysokość drzewa [m])
    - leafs (liczba liści),
    oraz metody:
    - grow_up (rośnij wzwyż), która przyjmie argument liczbowy w postaci wysokości do dodania,
        a następnie zwiększy wysokość tego drzewa
    - grow_wide (rośnij wszerz), która przyjmie argument liczbowy w postaci liczby nowych liści,
    - show, która wyświetli na ekranie wszystkie parametry drzewa wraz z ich wartościami
    - Utworzyć 5 takich drzew (5 obiektów) i wyświetlić ich stan wewnętrzny, a następnie dla dwóch
        wybranych drzew zwiększyć wysokość i jeszcze raz wyświetlić ich stan wewnętrzny
    """
    def __init__(self, name, height, leafs):
        self.name = name
        self.height = height
        self.leafs = leafs

    def grow_up(self, x: int):
        self.height += x

    def grow_wide(self, x: int):
        self.leafs += x

    def show(self):
        pprint(self.__dict__)


trees_list = []
