import math


def calc_area(diameter: float) -> float:
    return math.pi * pow(diameter/2, 2)


def calc_price(toppings_count: int, area: float) -> float:
    return (.005 * area) + (toppings_count * 2)


class Pizza:
    __slots__ = (
        '__price',
        '__toppings',
        '__diameter',
    )

    @property
    def diameter(self) -> float:
        return self.__diameter

    @diameter.setter
    def diameter(self, value: float) -> None:
        if value < 20:
            print('Błędny promień')
            exit(-10)

        self.__diameter = value

        area = calc_area(value)
        self.__price = round(calc_price(len(self.__toppings), area), 2)

    @property
    def toppings(self) -> list[str]:
        return self.__toppings.copy()

    @property
    def price(self):
        return self.__price

    def __init__(self, toppings: list[str], diameter: float) -> None:
        self.__toppings = toppings
        self.diameter = diameter

    def __str__(self):
        result = f'Pizza:\n' \
                 f'średnica: {self.__diameter}\n'

        if self.__toppings:
            toppings = ', '.join(self.__toppings)
            result += f'dodatki: {toppings}\n'

        result += f'cena: {self.__price}'

        return result

    def __add__(self, other):
        return Pizza(
            self.toppings + other.toppings,
            max(self.diameter, other.diameter),
        )

    def add_topping(self, topping: str) -> None:
        self.__toppings.append(topping)
        self.__price += 2
