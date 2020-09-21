# makeSet.py

mylist = [1, 1, 1, 2, 2, 2, 3, 3 ,3, 4, 4, 5]
print(len(mylist))

myset = set(mylist)
print(myset)

newlist = list(myset)
print(newlist)

set1 = set([1,2,3])
print(set1)
print("-" * 30)

set1.add(4)
print(set1)
print("-" * 30)

set1.update([5, 6, 7])
print(set1)
print("-" * 30)

set1.remove(4)
print(set1)
print("-" * 30)

set3 = set([1, 2, 3, 4])
set4 = set([3, 4, 5, 6])

set5 = set3.intersection(set4)
print(set5)
print("-" * 30)

set6 = set3.union(set4)
print(set6)
print("-" * 30)

set7 = set3.difference(set4)
print(set7)
print("-" * 30)

set8 = set4.difference(set3)
print(set8)
print("-" * 30)

# 다음은 어떤 자료 구조로 표현하면 좋을 까요?
# 1) 회원 가입 정보 (아이디는 "hong" 이름은 "홍길동" ...) (dict)
# 2) 로또 번호 생성기 (set)
# 3) 게시물의 제목 정보 (list)