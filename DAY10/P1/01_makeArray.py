# 01_makeArray.py

# 배열 생성하는 여러가지 방법

import numpy as np

# zeros : 요소가 0인 행렬/배열을 생성해주는 함수
print(np.zeros(3))
print('-' * 30)

arr = np.zeros((2,2))
print(arr)
print('-' * 30)

arr2 = np.ones((3,2))
print(arr2)
print('-' * 30)

# 연립 방정식을 풀고자 할 때 사용(가우스 소거법)
# 크기가 3인 단위 행렬을 만들어 줌
# 정방 행렬 : 행과 열의 크키가 같은 행렬
arr3 = np.eye(3)
print(arr3)
print('-' * 30)

# 모든 요소의 값이 5인 2행 2열의 행렬을 생성
arr4 = np.full((2,2), 5)
print(arr4)
print('-' * 30)


print('finished')