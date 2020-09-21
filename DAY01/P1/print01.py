# print01.py
# 샵을 붙이면 주석
print('동해물과' '백두산이')
print("동해물과" "백두산이" "마르고" "닳도록")
#콤마 붙이면 띄워쓰기 가능
print('동해물과', '백두산이', '마르고', '닳도록')

# end=매개변수(옵션) end = 기본값은 엔터 키
# end를 입력하면 엔터 키의 기본값은 사라지고, 지정한 값으로 대체됨
print('안녕하세요', end=' ')
print('홍길동님')

# input() 함수 : 값을 입력 할수 있는 함수
# 기본적으로 입력된 데이터는 문자열로 인식함
print("이름을 입력")
name = input()
age = input ("나이 입력")
print("이름 :", name, "나이 :", age)

# 데이터 형변환 : 바꿀타입(바꿀데이터)
newage = int(age) + 5
print("5년뒤 나이 :" + str(newage))

kor = int(input('국어 점수 입력 :'))
eng = int(input('영어 점수 입력 :'))
math = int(input('수학 점수 입력 :'))
total = kor + eng + math
print("총점:", total)