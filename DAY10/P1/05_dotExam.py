# 05_dotExam.py

# 행렬과 벡터의 연산(dot 함수)

import numpy as np

arrX = np.array([[1, 2], [3, 4]])
arrY = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# 벡터의 내적 : 벡터 각 요소들의 곱셈 결과의 총합
print('벡터의 내적')
print(v.dot(w))      # 9*11 + 10*12
print()
print(np.dot(v,w))
print()

print('행렬과 벡터의 곱셈')
print(np.dot(arrX, v))    # 1*9 +2*10 / 3*9 + 4*10
print()

print('행렬과 행렬의 곱셈')
print(np.dot(arrX, arrY))
print()

aa = np.array([[1,2,3],[4,5,6,]])
print(aa.shape)

bb = np.array(([1,0],[3,1],[0,3]))

print(np.dot(aa,bb))
print()

cc = np.array([[5,8], [9,3]])
dd = np.array([[7,4], [7,5]])

result = np.add(cc, dd)             # 덧셈
print(result)
print()

result = np.subtract(cc, dd)        # 뺄셈
print(result)
print()

result = np.multiply(cc, dd)        # 곱셈
print(result)
print()

result = np.divide(cc, dd)          # 나눗셈
print(result)
print()