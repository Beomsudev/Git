# indexingSlicing.py

#       0123456789a
str1 = "Hello Korea"
print(str1[0])
print(str1[0], str1[6])
# 마이너스가 나오는 경우 오른쪽에서 카운터
print(str1[-3])

# 문제 위의 str1에서 'KHa'를 출력해 보세요.
print(str1[6], str1[0], str1[-1], sep='')

# 슬라이싱 : 전체 내용 중에서 일부 내용을 연속적으로 추출하는 것
# [from:to:step] : step의 기본 값은 1(생략하면 1), from의 기본 값은 0
# from <= 슬라이싱 < to
print(str1[0:5])
print(str1[:5])
print(str1[0:5:2])

#      0123456789abcd
ssn = '881120-1234567'
print("앞자리", ssn[0:6])
print("뒷자리", ssn[7:14]) # 맨 뒷자리까지 추출하는 경우 뒤에 번호는 생략 가능(ex [7:]

aa = ssn[7]

if aa == '1' or  aa == '3':
    print("남")
else:
    print("여")
#           0     1    2     3     4     5     6
#          -7    -6   -5    -4    -3    -2    -1
rainbow = ['빨', '주', '노', '초', '파', '남', '보']

another = rainbow[4:7]
print(another)

even = rainbow[0:7:2]
print(even)

odd = rainbow[1:7:2]
print(odd)

abcd = rainbow[-3:-1]
print(abcd)