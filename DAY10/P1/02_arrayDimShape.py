# 02_arrayDimShape.py

# 배열의 크기(dimension)와 형상(shape)
import numpy as np

# ndarray : n(정수) d(차원) array(행렬/배열)
data = np.array([[1,2,3], [4,5,6]])
data2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(type(data))

print('rank(차원) : ', data.ndim)     # ndim 속성 이라고함

print('형상 : ', data.shape)          # shape 속성

print('몇행? : ', data.shape[0])

print('몇열? : ', data.shape[1])

# int8, int16, int32, float64
print('자료형 : ', data.dtype)         # dtype 속성

print(data)

print(data[0][1], data[1][1], data[1][2])

print('-' * 30)

print( data * data)
print('-' * 30)

mylist = [1, 2]
print(mylist+mylist)
print('-' * 30)

print( data * 10)
print('-' * 30)

print( data + data)
print('-' * 30)

print( 1 / data)
print('-' * 30)

print( data ** 0.5)     # 루트
print('-' * 30)