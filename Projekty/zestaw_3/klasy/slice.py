from .pizza import Pizza


class Slice(Pizza):
    __slots__ = ('__how_many_slices', )

    @property
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, value: int) -> None:
        if (not 4 <= value <= 12) or (value % 2):
            print('Błędna ilość kawałków')
            exit(-10)

        self.__how_many_slices = value

    @how_many_slices.getter
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    def __init__(self, toppings: list[str], diameter: float, how_many_slices: int) -> None:
        super().__init__(toppings, diameter)

        self.how_many_slices = how_many_slices

    def __str__(self):
        result = super().__str__()

        result += f'\nkawałki: {self.__how_many_slices}\n' \
                  f'cena za kawałek: {self.part_price(1)}'

        return result

    def part_price(self, ordered_slices: int) -> float:
        return round(self.price * (ordered_slices / self.how_many_slices), 2)
