# 11_myDeviation.py

# list의 표준 편차 구하기
# 다음 리스트를 이용하여 표준 편차를 구해주는 함수 deviation을 구현하시오

import math
data = [10, 20, 30, 40]
def deviation(data):
    total = 0
    for idx in data:
        aaa = idx ** 2
        total += aaa
        bunsan = total/len(data)
        deviation_a = math.sqrt(bunsan)

    print("-" * 30)
    print("총   합 : ", total)
    print("분   산 : ", bunsan)
    print("표준편차 : ", deviation_a)


mylist01 = [20, 30, 40, 50]
mylist02 = [1, 2, 3, 4, 5, 6]

print(deviation(mylist01))
print(deviation(mylist02))
