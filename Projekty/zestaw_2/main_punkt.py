from klasy_punkty.punkt import Punkt


def main():
    a: Punkt = Punkt(5, 9)
    print(f'Utworzony punkt: {a}')
    a.move(-2, 6)
    print(f'Przesuniety punkt: {a}')
    print(f'Wspolrzedna x: {a.x}, wspolrzedna y: {a.y}')
    print(a.__dict__)


if __name__ == "__main__":
    main()
