# for01.py
# range() 함수
# range(start, end, step)
# range(시작<=  종료<  단계)

for idx in range(1, 11):
    print(idx)
print("-" * 30)

for idx in range(11):
    print(idx)
print("-" * 30)

for idx in range(1, 10, 2):
    print(idx)
print("-" * 30)

for idx in range(10, 1, -1):
    print(idx)
print("-" * 30)

# 1부터 10까지의 총합 구하기
total = 0

for xxx in range(1,11) :
    total += xxx

print("총합 : %d" %(total))

# 문제 1 : 1 + 4 + 7 + 10 + ... + 100 = 1717 (3씩 커진 값)
# 문제 2 : 97 + 92 + 87 + ... 7 + 2 = 990 (5씩 줄어든 값

q1 = 0
for q1_n in range(1, 101, 3) :
    q1 += q1_n
print("문제 1의 총합은 %d 입니다." %(q1))

q2 = 0
for q2_n in range(97, 1, -5) :
    q2+= q2_n
print("문제 2의 총합은 %d 입니다." %(q2))

# 문제 3 : 1*1 + 6*6 + 11*11 + ... + 96*96 = 63670

q3 = 0
for q3_n in range(1,97,5) :
    q3 += q3_n*q3_n #or q3 += pow(q3_n,2) or q3 += q3_n **2
print("문제 3의 총합은 %d 입니다." %(q3))

# 문제 4 : 사용자가 숫자를 하나 입력 받고, 1부터 해당 수까지의 총합을 구하시요.
"""
q4 = 0
q4_i = int(input("숫자를 입력 하세요."))
for q4_n in  range(1, q4_i+1, 1) :
    q4 += q4_n

print("출력 결과 1부터 %d까지의 합은 %d입니다." %(q4_i, q4))
"""

print(abs(-15)) # abs = 절대 값으로 변경 해주는 함수.

# 문제 4-1 : 사용자가 숫자를 하나 입력 받고, 1부터 해당 수까지의 총합을 구하시요.

q4 = 0
q4_i = abs(int(input("숫자를 입력 하세요.")))
for q4_n in  range(1, q4_i+1, 1) :
    q4 += q4_n

print("출력 결과 1부터 %d까지의 합은 %d입니다." %(q4_i, q4))
