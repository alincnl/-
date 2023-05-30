from __future__ import print_function

class Accountant():
    def __init__(self, name):
         self.__name = name

    def give_salary(self, worker):
        if isinstance(worker, Pupa):
            worker.take_salary(125)
        if isinstance(worker, Lupa):
            worker.take_salary(100)


class Pupa():
    def __init__(self, name):
         self.name = name
         self.cash = 0

    def do_work(self, filename1, filename2):
        matrix1 = []
        matrix2 = []

        with open(filename1,"r") as f:
            while True:
                line = f.readline()
                if line=='\n':
                    break
                matrix1.append(line.split())

        with open(filename2,"r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                matrix2.append(line.split())

        if len(matrix1) !=  len(matrix2) and len(matrix1[0]) !=  len(matrix2[0]):
            raise IndexError('dim matrix1 != dim matrix2')
        else:
            matrix3 = [[0 for j in range(len(matrix1[0]))] for i in range (len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    print(int(matrix1[i][j]) + int(matrix2[i][j]),end=' ')
                print()

    def take_salary(self, num):
        self.cash += num

    def name(self):
        return self._name

    def cash(self):
        return self._cash


class Lupa():
    def __init__(self, name):
         self.name = name
         self.cash = 0

    def do_work(self, filename1, filename2):

        matrix1 = []
        matrix2 = []

        with open(filename1,"r") as f:
            while True:
                line = f.readline()
                if line=='\n':
                    break
                matrix1.append(line.split())

        with open(filename2,"r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                matrix2.append(line.split())

        if len(matrix1) !=  len(matrix2) and len(matrix1[0]) !=  len(matrix2[0]):
            raise IndexError('dim matrix1 != dim matrix2')
        else:
            matrix3 = [[0 for j in range(len(matrix1[0]))] for i in range (len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    print(int(matrix1[i][j]) - int(matrix2[i][j]),end=' ')
                print()

    def take_salary(self, num):
        self.cash += num

    def name(self):
        return self.name

    def cash(self):
        return self.cash


Employer = Accountant("Stepan")

Alina = Pupa("Alina")
Alina.do_work("ex1.txt","ex2.txt")

Employer.give_salary(Alina)
print(Alina.cash)

Ksusha = Lupa("Ksusha")
Ksusha.do_work("ex1.txt","ex2.txt")

Employer.give_salary(Ksusha)
print(Ksusha.cash)

