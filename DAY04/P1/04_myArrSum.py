# 04_myArrSum.py

#리스트의 모든 요소들의 합을 구해주는 함수 arrsum을 만들어 보세요.

# 내가 푼거
# ----------------------------------
def arrsum(a):        # 했갈리는 부분 매개변수 a는 위치만 알려준다고 생각, a를 list 데이터를 넣으면 자동으로 list인식됨
    return sum(a)

list01 = [1, 2, 3]
print(arrsum(list01))
# ----------------------------------

# 선생님이 푼거
# ----------------------------------
def arrsum02(list1):
    total = 0
    for item in list1:
        total += item
    return total

list01 = [1, 2, 3, 4]
print(arrsum02(list01))

# 튜플
mydata = (1, 2, 3, 3, 3)
print(arrsum(mydata))

# 집합

myset = set(mydata)
print(arrsum(myset))