# fomatFunc.py
su = 3
fruit = "사과"

print('positional argument') # 인덱스 기반 매개 변수 대입
str1 = "나는 {}를 {}개 먹었습니다."
print(str1.format(fruit, su))

str2 = "나는 {0}를 {1}개 먹었습니다."
print(str2.format(fruit, su))

str3 = "나는 {1}를 {0}개 먹었습니다."
print(str3.format(su,fruit ))

print('keyword argument') #문자로 지정하는 type
str4 = "나는 {abc}를 {defg}개 먹었습니다."
print(str4.format(defg=su, abc=fruit))

# 2가지 혼합 방식
str5 = "나는 {abc}를 {}개 먹었습니다."
print(str5.format(su, abc=fruit))

# positional argument가 먼저 와야함 !!!
# str6 = "나는 {abc}를 {}개 먹었습니다."
# print(str6.format(abc=fruit, su))

name = "김철수"
fruit = "사과"
su1 = 8

# 서식 지정자 : %s(string) %d(decimal) %f(float) 실수
#             %c(문자1개), %o(8진수), %
myformat = "%s가 %s를 %d개 먹었습니다."
print(myformat % (name, fruit, su1))

# 문제 4곱하기 9는 36입니다.
su1 = 4
su2 = 9

result = "{} 곱하기 {}는 {} 입니다."
print(result.format(su1,su2,(su1*su2)))

# pow(a, b) : a의 b승
# 문제 2.0의 10.0승은 1024.0입니다.
#print(pow(5, 2))
su1 = 2.0
su2 = 10.0
myformat = "%.2f의 %.2f승은 %f입니다."
# float는 소수점 6자리 까지 표현
# 더 적게 하고 싶으면 이렇게 %.2f
print(myformat % (su1, su2, pow(su1, su2)))

rate = 0.4567
print( "비율 : %.3f%%" % (100*rate))