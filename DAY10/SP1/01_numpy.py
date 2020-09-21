import numpy as np
#
# print(np.zeros(5))
# print(type(np.zeros(5)))
# print('='*30)
#
# arr = np.zeros((2,2))
# print(arr)
# print(type(arr))
# print('='*30)
#
# arr2 = np.ones((3,2))
# print(arr2)
# print('='*30)
#
# arr3 = np.eye(3)
# print(arr3)
# print('='*30)
#
# arr4= np.full((2,2), 5)
# print(arr4)
# print('='*30)
#
# data = np.array([[1,2,3], [4,5,6], [4,5,6], [4,5,6]])
# print(data)
# data2 = np.array([[1,2,3]])
# print(type(data))
#
# print('rank(차원) : ', data.ndim)     # ndim 속성 이라고함
#
# print('형상 : ', data.shape)          # shape 속성
#
# print('몇행? : ', data.shape[0])
#
# print('몇열? : ', data.shape[1])
# print('='*30)
#
# # int8, int16, int32, float64
# print('자료형 : ', data.dtype)         # dtype 속성
#
# print(data)
#
# print(data[0][1], data[1][1], data[1][2])
#
# print('-' * 30)
#
# print( data * data)
# print('-' * 30)
#
# mylist = [1, 2]
# print(mylist+mylist)
# print('-' * 30)
#
# print( data * 10)
# print('-' * 30)
#
# print( data + data2)
# print('-' * 30)
#
# print( 1 / data)
# print('-' * 30)
#
# print( data ** 0.5)     # 루트
# print('-' * 30)
#
# print('='*30)
#
# data = np.array([[10,20], [30,40]])
# print(data)
# print('-' * 30)
#
# result = np.sum(data)                          # sum : 모든 요소의 합을 구함
# print(result)
# print(type(result))
# print('-' * 30)
#
# result = np.sum(data, axis=0)                  # axis=0 : 행을 따라가면서, 열 단위 합산
# print(result)
# print(type(result))
# print('-' * 30)
#
# result = np.sum(data, axis=1)                  # axis=1 : 열을 따라가면서, 행 단위 합산
# print(result)
# print('-' * 30)
#
# result = np.mean(data)                             # mean : 모든 요소의 평균
# print(result)
# print('-' * 30)
#
# result = np.min(data)                              # min : 최소값
# print(result)
# print('-' * 30)
#
# result = np.max(data)                            # max : 최대값
# print(result)
# print('-' * 30)
#
# result = np.max(data, axis=0)
# print(result)
# print('-' * 30)
#
# print('='*30)

#
# a = np.array([-1, 3, 2, -6])        # 1차원
# b = np.array([3, 6, 1, 2])
# print(a.ndim)
# print(a.shape)
#
# print('-' * 30)
#
# A = np.reshape(a, [2,2], order='C')
# print(A)
# print(A.ndim)
# print(A.shape)
#
# print('-' * 30)
#
# B = np.reshape(b, [2,2])
# print(B)
# print(B.ndim)
# print(B.shape)
# print('-' * 30)
#
# # matmul : MATrix MULtiply  행렬의 합
# result3_1 = np.matmul(A, B)
# result3_2 = np.matmul(B, A)
# print(result3_1)
# print('-' * 30)
#
# print(result3_2)
# print('-' * 30)
#
# b = np.reshape(b, [1,4])
# a = np.reshape(a, [1,4])
# b2 = np.transpose(b)    # 전치 함수 : 행과 열을 바꿈
#
# print(a)
# print('a' * 30)
#
# print(b)
# print('b' * 30)
#
# print(b2)
# print('-' * 30)
#
# result3_3 = np.matmul(a,b2)
# print(result3_3)
# print('-' * 30)

#
#
# arrX = np.array([[1, 2], [3, 4]])
# arrY = np.array([[5, 6], [7, 8]])
# v = np.array([9, 10])
# w = np.array([11, 12])
#
# # 벡터의 내적 : 벡터 각 요소들의 곱셈 결과의 총합
# print('벡터의 내적')
# print(v.dot(w))      # 9*11 + 10*12
# print()
# print(np.dot(v,w))
# print()
#
# print('행렬과 벡터의 곱셈')
# print(np.dot(arrX, v))    # 1*9 +2*10 / 3*9 + 4*10
# print()
#
# print('행렬과 행렬의 곱셈')
# print(np.dot(arrX, arrY))
# print()
#
# aa = np.array([[1,2,3],[4,5,6,]])
# print(aa.shape)
#
# bb = np.array(([1,0],[3,1],[0,3]))
# print('===========')
# print(np.dot(aa,bb))
# print()
#
# cc = np.array([[5,8], [9,3]])
# print(cc)
# dd = np.array([[7,4]])
# print(dd)
# print('===========')
#
# result = np.add(cc, dd)             # 덧셈
# print(result)
# print()
#
# result = np.subtract(cc, dd)        # 뺄셈
# print(result)
# print()
#
# result = np.multiply(cc, dd)        # 곱셈
# print(result)
# print()
#
# result = np.divide(cc, dd)          # 나눗셈
# print(result)
# print()

print('임의의 값으로 채워진 행렬 생성')
# random : 최소 0이상, 1미만의 숫자
result = np.random.random((2,2))
print(result)
print('-' * 20)

print('표준 편차가 1, 평균이 0인 정규 분포에서 표본 추출')
# randn : RADNom Normalization
result = np.random.randn(2, 3)
print(result)
print('-' * 20)

print('임의의 값으로 채워진 배열 생성')
result = np.random.rand(4, 4)
print(result)
print('-' * 20)

print('균등 분포에서 데이터 추출')
result = np.random.uniform(size=(3,3))
print(result)
print('-' * 20)

print('정수 0이상 5미만의 정수 추출')
result = np.random.randint(5)
print(result)
print('-' * 20)

result = np.random.randint(3, size=(4,4))
print(result)
print('-' * 20)

result = np.random.randint(0, 5, size=10)
print(result)
print('=' * 20)

# 문제 : 0, 1, 2 중에서 임의로 하나를 추출하는 동작을 5번 수행하여
# 나온 수의 총합을 구하시오

result = np.random.randint(0, 3, size=5)
print(result)
print(np.sum(result))
print('-' * 20)


# 시드 배정은 동일한 데이터를 샘플링하거나
# 머신 러닝시 동일한 결과를 한시적으로 추출해보고자 할 때 사용
seed = 1
np.random.seed(1)    # 랜덤 값에 시드 배정

print('0부터 9까지의 수를 임의로 섞어준다(안겹침)')
length = 10
result = np.random.permutation(length)
print(result)
print('-' * 20)

# 0 <= 값 < 5 사이의 임의의 수 3개 추출
result = np.random.choice(5, 3)
print(result)
print('-' * 20)

# 0 <= 값 < 5 사이의 임의의 수 3개 추출
#                                   0   1   2    3   4  각 숫자의 확률을 설정 ex 3 = 60퍼센트
result = np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
print(result)
print('-' * 20)