#2.2
def skal_mult(matrix1,matrix2):
    su = 0
    #скал€рное умножение
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            su += int(matrix1[i][j]) * int(matrix2[i][j])
    return su

def cut(matrix, column, row, initC, initR):
    #вырезаем патчи
    newm = [[0 for j in range(row)] for i in range (column)]
    for i in range(column):
        for j in range(row):
            try:
                newm[i][j] = matrix[initC + i][initR + j]
            except IndexError:
                return []
    return newm

def svertka(n,m):
    nx, ny = len(n), len(n[0])
    mx, my = len(m), len(m[0])

    if nx < mx or ny < my:
        return -543546
    matrix3 = [[0 for j in range(ny - my + 1)] for i in range (nx - mx + 1)]
    for i in range(nx - mx + 1):
        for j in range(ny - my + 1):
            newn = cut(n,mx,my,i,j)
            if newn == []:
                continue
            matrix3[i][j] = skal_mult(newn,m)
    return matrix3

matrix1 = []
matrix2 = []
with open("example.txt","r") as f:
   
    #чтение матриц
    while True:
        line = f.readline()
        if line == '\n':
            break
        matrix1.append(line.split())
    while True:
        line = f.readline()
        if not line:
            break
        matrix2.append(line.split())

    matrix3 = svertka(matrix1,matrix2)

    #запись в файл
    with open("out.txt", "w") as f1:
        if matrix3 == -543546:
            f1.write('bad size')
        else:
            for line in matrix3:
                for l in line:
                    f1.write(str(l))
                    f1.write(' ')
                f1.write('\n')
