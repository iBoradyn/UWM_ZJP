import pickle

from klasy_punkty.punkt import Punkt
from klasy_punkty.nazwany_punkt import NazwanyPunkt

points_list = [
    Punkt(1, 2),
    Punkt(2, 3),
    NazwanyPunkt(3, 4, 'punkt_1'),
    NazwanyPunkt(4, 5, 'punkt_2'),
]

with open('punkty.pkl', 'wb') as file:
    pickle.dump(points_list, file)

with open('punkty.pkl', 'rb') as file:
    print(pickle.load(file))
