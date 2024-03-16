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
        Null_solutions = []
        One_solution = []
        Two_solutions = []
        Three_solutions = []
        Four_solutins = []
        INF_solutions = []
        for i in all_comp:
            if len(i) == 2:
                e = Equation(*i)
                j = e.solve()
                amount = len(j)
                if amount == 0:
                    Null_solutions.append(i)
                elif amount == 1:
                    One_solution.append(i)
                elif j == 'infinity':
                    INF_solutions.append(i)
            if len(i) == 3:
                e = QuadraticEquation(*i)
                j = e.solve()
                amount = len(j)
                if amount == 0:
                    Null_solutions.append(i)
                elif amount == 1:
                    One_solution.append(i)
                elif amount == 2:
                    Two_solutions.append(i)
                elif j == 'infinity':
                    INF_solutions.append(i)
            if len(i) == 5:
                k = list(i)
                k.pop(3)
                k.pop(1)
                e = diquadratic(*k)
                j = e.solve()
                amount = len(j)
                if amount == 0:
                    Null_solutions.append(i)
                elif amount == 1:
                    One_solution.append(i)
                elif amount == 2:
                    Two_solutions.append(i)
                elif amount == 3:
                    Three_solutions.append(i)
                elif amount == 4:
                    Four_solutins.append(i)
                elif j == 'infinity':
                    INF_solutions.append(i)
        ALL_AMOUNT = [Null_solutions, One_solution, Two_solutions, Three_solutions, Four_solutins, INF_solutions]
        return ALL_AMOUNT


