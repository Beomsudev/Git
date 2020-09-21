# adultSsnCheck.py



"""
출력 결과
이름 : 김철수
주민 번호 : 121225-3456789
성별 : 남자         # 맨 뒷 첫자리 1,3은 남자 / 2,4는 여자
나이 : 8세          # (20년도 - 태어난 년도)
체크 : 미성년자      # (19세 이상이면 성년
"""
# 0  1  2  3  4  5    6  7  8  9  a  b  c  d
# 1, 2, 1, 2, 2, 5, , -, 3, 4, 5, 6, 7, 8, 9
""" 내 답
name = "김철수"
ssn = "121225-3456789"

sex = ssn[7]
age = 20 - int(ssn[0:2])

print("이름 : ", name, sep="")
print("주민 번호 : ", ssn, sep="")

# 밑에 거 이렇게 표현 가능 if sex in ["1", "3"]
if sex == 1 or 3 :
    print("성별 : 남자")
else :
    print("성별 : 여자")

print("나이 : ", age)

if age >= 19 :
    print("체크 : 성년")
else :
    print("체크 : 미성년자")
"""

name = "김철수"
ssn = "121225-3456789"

sex = ssn[7]
# 이 부분 다시 생각 해서 풀어 보기! 답보지 말고.
birth_year = int(ssn[0:2])
birth_year_full = int()

if sex == 1 or 3 :
    birth_year_full = 2000 + birth_year
else :
    birth_year_full = 1900 + birth_year

age = 2020 - birth_year_full

print("이름 : ", name, sep="")
print("주민 번호 : ", ssn, sep="")

# 밑에 거 이렇게 표현 가능 if sex in ["1", "3"]
if sex == 1 or 3 :
    print("성별 : 남자", sep="")
else :
    print("성별 : 여자", sep="")

print("나이 : ", age, sep="")

if age >= 19 :
    print("체크 : 성년", sep="")
else :
    print("체크 : 미성년자", sep="")
