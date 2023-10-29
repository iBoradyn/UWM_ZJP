from klasy_punkty.punkt import Punkt
from klasy_punkty.nazwany_punkt import NazwanyPunkt


def main():
    a: NazwanyPunkt = NazwanyPunkt(3, 4, "latarnia")
    print(a)
    a.move(-2, 5)
    print(a)
    print(a.__dict__)
    print(type(a))
    b: NazwanyPunkt = NazwanyPunkt(7, 0, "morze")
    c: Punkt = Punkt(5, 9)

    print(issubclass(Punkt, Punkt))
    print(issubclass(Punkt, NazwanyPunkt))
    print(issubclass(NazwanyPunkt, Punkt))

    print(isinstance(a, Punkt))
    print(isinstance(a, NazwanyPunkt))
    print(isinstance(c, NazwanyPunkt))
    print(dir(a))
    del a
    print(a)


if __name__ == "__main__":
    main()
