# stringFunction.py
# 문자열 관련 함수 다뤄 보기

mystring = "Hello python!"
print('길이 :', len(mystring))
print('포함갯수 :', mystring.count('o'))
print('검색위치0 :', mystring.find('e'))
print('검색위치1 :', mystring.find('o', 6))
print('검색위치2 :', mystring.rfind('l'))

print('문자열 치환1 :', mystring.replace('l', 't'))
print('문자열 치환2 :', mystring.replace('l', 't', 1))
print('문자열 치환3 :', mystring.replace('l', 'blue'))

# sep 옵션은 기본 값 띄워 쓰기.
#
mystring = '     가나     다라     '
print("공백 제거 1 : [", mystring.strip(), "]", sep='')
print("공백 제거 2 : [", mystring.lstrip(), "]", sep='')
print("공백 제거 3 : [", mystring.rstrip(), "]", sep='')

mystring = 'xxxHello'
print("공백 제거4 : [", mystring.strip('x'),"]", sep="")

mystring = "hello python"

print("대문자 :", mystring.upper())
print("소문자 :", mystring.lower())
print("첫 글자만 대문자 :", mystring.capitalize())

# delimiter : 문자열을 나눠주는 구분자
# split 함수는 기본 값으로 공백을 이용하여 문자를 분리해준다.
print("문자열 분리 :", mystring.split())

mystring = '소녀시대/빅뱅/원더걸스'
print("문자열 분리 2 : ", mystring.split('/'))

mystring = 'hello_python.xls'

print("시작 여부 :", mystring.startswith("H"))
print("종료 여부 :", mystring.endswith(".ppt"))


print("시작 여부 :", mystring.upper().startswith("H")) #메소드 체이닝

mylist = ["삼성", "엘지", "sk"]
print("".join(mylist))

str = input("문자입력")
pos = 2
munja = str[pos] #인덱싱 (중요!!)
print(munja)

munja = str[pos] #인덱싱 (중요!!)
print(munja)

print("대문자 여부 : ", munja.isupper())
print("소문자 여부 : ", munja.islower())
print("숫자 여부 : ", munja.isdigit())

#프로그램 내부에서 아스키 코드로 변경된 다음, 비교 연산 진행
print(munja > "s") # 문자는 r로 인덱싱 상태(korea에서 2로인덱싱)

#복습 필!!!!!
print(munja >= "A" and munja <="Z")
print(munja >= "a" and munja <="z")
print(munja >= "0" and munja <="9")

print(ord(munja))
print(ord("A"))
print(ord("a"))
print(ord("0"))

