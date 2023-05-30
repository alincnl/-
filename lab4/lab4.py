import numpy as np
import numpy.ma as ma
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('n', help="Enter length", type=int)
args = parser.parse_args()
print(args)

#filename1, filename2 = input(), input()
P = float(input())

if P > 1 or P < 0:
    raise ValueError(f'Invalid value')
real_data, sint_data = [], [] 

with open("file1.txt", "r") as f:
    real_data = f.readline()
    real_data = (list(map(int, real_data.split())))
with open("file2.txt", "r") as f:
    sint_data = f.readline()
    sint_data = (list(map(int, sint_data.split())))

real_data, result = np.array(real_data), np.array([])
kolvo = int(P*len(real_data))
print("real:", real_data)
print("synthetic:", sint_data)
    
#4.1
result = real_data.copy()

if P!=0:
    c_ind = random.sample(range(0, len(sint_data)), kolvo)
    c = np.take(sint_data, np.sort(c_ind)) #на что будем менять
    a = random.sample(range(0, len(real_data)), kolvo) #изменяемые индексы

    result[np.sort(a)] = c #замена
print("1ST WAY:", result)

#4.2
if P!=0:
    real_data = real_data.tolist() #выбираем изменяемые элементы
    replace_real = random.sample(real_data, kolvo)

    replace_sint_ind = random.sample(range(0, len(sint_data)), kolvo)
    replace_sint = np.take(sint_data, np.sort(replace_sint_ind)) #заменяющие элементы
    print(replace_real, replace_sint)

    mask = np.in1d(real_data,replace_real) #маска
    print(mask)

    real_data = np.array(real_data)
    np.place(real_data,mask,replace_sint) #замена
print("2ND WAY:", real_data)
