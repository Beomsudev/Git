# 05_makeIterable01.py

# Iterable : 반복 할 수 있는, 반복 가능한
# list, tuple, dict, 문자열 = 목록을 1개이 상가진 데이터 (Iterable data 라고도 함)


# list comprehension (list를 만들때 for문을 사용하면 이렇게 부른다)
# set, dict 등 도 있음
mylist01 = [idx for idx in range(1, 5)]
print(mylist01)
print("-" * 30)

mylist02 = [2 * idx for idx in range(1, 5)]
print(mylist02)
print("-" * 30)

mylist03 = [idx for idx in range(1, 101, 3)]
print(mylist03)
print(sum(mylist03))
print("-" * 30)

mylist04 = [idx for idx in range(1, 101, 3) if idx % 10 == 0]
print(mylist04)
print("-" * 30)

# 1 부터 10까지의 정수 중에서 3의 배수가 아닌 수들의 총합
mylist05 = [idx for idx in range(1, 11) if idx % 3 != 0]
print(mylist05)
print(sum(mylist05))
print("-" * 30)

# 중첩 for
mylist06 = [x * y for x in range(2, 10) for y in range(1, 10)]
print(mylist06)
print(sum(mylist06))
print("-" * 30)

# 중첩 for
mylist06 = [x * y for x in range(2, 10) for y in range(1, 10)]
print(mylist06)
print(sum(mylist06))
print("-" * 30)


mylist = [("김", 10), ("이", 20), ("최", 30)]

mydict = {data[0]:data[1] for data in mylist} # 이해하는 데 좀 걸림 다시 확실하게 복습 !
print(mydict)
print("-" * 30)

# 문제 : students를 사용하여 다음과 같은 사전을 만들어 보세요. / 금방풀었음
# "이순신":(80, 90), "김유신":(70, 40)
students = [("이순신", 80, 90), ("김유신", 70, 40)]

mydict = {data[0]:data[1:3] for data in students} # 이해하는 데 좀 걸림 다시 확실하게 복습 !
print(mydict)
print("-" * 30)
