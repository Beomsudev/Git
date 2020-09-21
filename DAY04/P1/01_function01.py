# 01_function01.py
# 함수 : 반복적인 행위를 수행하기 위하여 미리 작성해 놓은 소스 코드
# 매개 변수 : 함수의 소괄호 부분에 입력해주는 값
# ex) sum(2, 3) 에서 "2, 3"
# 매개 변수 = 인자 = 인수 = argument = parameter
# 함수의 종류 : 내장 함수(abs, pow, sum, min 등등)
#              사용자 정의 함수

# 함수를 작성하는 절차
# step 1 : 함수 구현
# def = define의 줄임말.
# 함수 이름은 임의로 작성 가능
# return 구문은 데이터를 반환할 때 사용하고, 옵션 사항임.
# return 구문을 사용 하지 않으면 None이 반환됨.
# None 키워드는 부정적인 용어, void, empty, no 등의 의미로 보면됨
""""
def 함수이름(매개변수1, 매개변수2, ...)    ----> def = define
    하고자 하는 일을 작성
    [return 반환할 데이터 명시]
"""

# step 2 : 함수 호출

# 어떠한 숫자를 입력하면 5를 더해주는 함수 구현
def plus5(su) :     #함수의 정의(구현) (step1)
    return su + 5


su1 = 14
result = plus5(su1) #함수 호출 (step2)
print("결과 01 : {}".format(result))
print("결과 02 : {}".format(plus5(100))) #함수 호출 (step2)

for idx in range(3, 12, 4):
    print(plus5(idx))

print("-" * 30)

mylist = [10, 20, 30]

for aaa in mylist :
    bbb = plus5(aaa)
    print(bbb)
print("-" * 30)

mytuple = (4, 8, 12)

for aaa in mytuple :
    bbb = plus5(aaa)
    print(bbb)