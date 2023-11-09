from klasy.pizza import Pizza
from klasy.slice import Slice


def main():
    # Test klasy Pizza
    p_1 = Pizza(['sos pomidorowy', 'ser'], 20)
    p_2 = Pizza(['szynka', 'ananas', 'kurczak'], 25)

    print('Pizza 1:')
    print(p_1)
    print('\nPizza 2:')
    print(p_2)

    print('\nPizza 1 po zmianach:')
    p_1.diameter = 35
    p_1.add_topping('salami')
    print(p_1)

    print('\nCena pizzy 1:')
    print(p_1.price)

    print('\nDodanie pizzy 1 i 2:')
    print(p_1 + p_2)

    # Test klasy Slice
    s_1 = Slice(['sos pomidorowy', 'ser'], 20, 6)

    print('\nKawałek 1:')
    print(s_1)

    print('\nCena za 5 kwawłków:')
    print(s_1.part_price(5))


if __name__ == "__main__":
    main()
