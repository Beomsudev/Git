# listTest3.py

# 중첩 리스트
# 중첩된 갯수만큼 대괄호 사용
saram01 = ["hong", "홍길동", 20, "용산"]
saram02 = ["kim", "김철수", 30, "마포"]
saram03 = ["kang", "강남", 40, "구로"]

mylist = []
mylist.append(saram01)
mylist.append(saram02)
mylist.append(saram03)
print(mylist)

print(mylist[1][2])

mylist[2][1] = "강호동"

print(mylist)

# 문제 세 사람의 평균 나이 구하기

total = mylist[0][2] + mylist[1][2] + mylist[2][2]
count_people = len(mylist)
average = total/count_people
print("세 사람 나이의 평균 : %.2f"% (average))

# "홍길동$김철수$강호동" 출력해보기

name_people = [mylist[0][1],mylist[1][1],mylist[2][1]]
print("$".join(name_people))
