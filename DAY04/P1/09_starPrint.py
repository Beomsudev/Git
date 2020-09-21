# 09_starPrint.py

# showStar() 함수를 이용하여 별을 su개 만큼 출력하는 프로그램을 만드시오
# 만약 매개변수를 입력하지 않으면 10개를 출력 하시오

def showStar(su=10):
    if su <= 0:
        su = -su
    print("*" * su)

a = int(input("숫자를 입력하세요 : "))
print(showStar(a))

print(showStar())

print("-" * 30)
for idx in range(1, 11):
    showStar(idx)