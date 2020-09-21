# 03_nempyEx01.py

import numpy as np

data = np.array([[10,20], [30,40]])
print(data)
print('-' * 30)

result = np.sum(data)                          # sum : 모든 요소의 합을 구함
print(result)
print('-' * 30)

result = np.sum(data, axis=0)                  # axis=0 : 행을 따라가면서, 열 단위 합산
print(result)
print('-' * 30)

result = np.sum(data, axis=1)                   # axis=1 : 열을 따라가면서, 행 단위 합산
print(result)
print('-' * 30)

result = np.mean(data)                             # mean : 모든 요소의 평균
print(result)
print('-' * 30)

result = np.min(data)                              # min : 최소값
print(result)
print('-' * 30)

result = np.max(data)                            # max : 최대값
print(result)
print('-' * 30)

result = np.max(data, axis=0)                  
print(result)
print('-' * 30)

print('finished')