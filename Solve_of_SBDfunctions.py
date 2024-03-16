from besquarefunc import QuadraticEquation
from diquadraticfunc import diquadratic
from squarefunc import Equation

class Solver:
    def __init__(self, argu):
        self.argu = argu

    @staticmethod
    def from_input_file(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        all_comp = []
        for line in lines:
            arguments = [float(x) for x in line.strip().split()]
            all_comp.append((arguments))

        return all_comp


    @staticmethod
    def sort_argu(all_comp):

        for i in all_comp:
            if len(i) == 2:
                e = Equation(*i)
                print(e)
                return e.solve()
            if len(i) == 3:
                e = QuadraticEquation(*i)
                print(e)
                return e.solve()
            if len(i) == 5:
                k = list(i)
                k.pop(3)
                k.pop(1)
                e = diquadratic(*k)
                print(e)
                return e.solve()

