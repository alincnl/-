##2.1
#def mult(matrix1,matrix2):
#    #проверка на то, что количество столбцов первой матрицы равно количеству строк второй
#    if len(matrix1[0])!= len(matrix2):
#        return -543546

#    matrix3 = [[0 for j in range(len(matrix2[0]))] for i in range (len(matrix1))]

#    #умножение
#    for i in range(len(matrix1)):
#        for j in range(len(matrix2[0])):
#            s = 0
#            for k in range(len(matrix1[0])):
#                s += int(matrix1[i][k]) * int(matrix2[k][j])
#            matrix3[i][j] = s
#    return matrix3

#matrix1 = []
#matrix2 = []
#with open("example.txt","r") as f:
   
#    #чтение матриц
#    while True:
#        line = f.readline()
#        if line=='\n':
#            break
#        matrix1.append(line.split())
#    while True:
#        line = f.readline()
#        if not line:
#            break
#        matrix2.append(line.split())

#    matrix3 = mult(matrix1,matrix2)

#    with open("out.txt", "w") as f1:
#        if matrix3 != -543546:
#            for line in matrix3:
#                for l in line:
#                    f1.write(str(l))
#                    f1.write(' ')
#                f1.write('\n')
#        else:
#            f1.write('bad size. column /= row')

#4

stroka = 'City is the capital of Country'
news = stroka.split(' ')

data = dict(City = 'London', Country = 'Great Britain')
print(data.keys())

for i in range(len(news)+1):
    if news[i] in data:
        news[i] = data[i]
print("Ќова€ строка:", news)