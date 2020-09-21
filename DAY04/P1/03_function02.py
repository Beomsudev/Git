# print(mylist_absolute).py

# 두 정수의 합을 구해주는 함수를 구현하고 테스트 하세요.
# add(5, 6) -> 11
# add(100, 200) -> 300


def pplus(a, b):
    return a + b

a = int(input("a 입력 : "))
b = int(input("b 입력 : "))
c = pplus(a, b)
print(c)