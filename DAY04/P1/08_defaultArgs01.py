# 08_defaultArgs01.py

# 매개 변수가 2개이고, 둘다 필수 사항이다.


def func01(a, b):
    return 2*a+b

print(func01(3, 5))

# print(func01())
# --> TypeError : TypeError: func01() missing 2 required positional arguments: 'a' and 'b'
# 필수 매개 변수 2개가 누락

# print(func01(3, 5, 5))
# --> TypeError : TypeError: func01() takes 2 positional arguments but 3 were given
# 매개 변수 갯수 초과

# 옵션 매개 변수 (필수 사항이 아니다.)
# 입력되지 않으면 기본 값을 사용한다.
def func02(a=2, b=1):
    return 2*a+b

# positional arguments(위치 기반 매개 변수)
print(func02())
print("-" * 30)

print(func02(3))
print("-" * 30)

print(func02(3, 5))
print("-" * 30)

# keyword arguments(키워드 기반 매개 변수)
print(func02(b=2, a=1))
print("-" * 30)

print(func02(2, b=1))
print("-" * 30)

# 포지셔널과 키워드를 섞어서 사용 할때에는 포지셔널이 먼저 와야 한다!
# print(func02(a=1, 2))
# print("-" * 30)

print("finished")