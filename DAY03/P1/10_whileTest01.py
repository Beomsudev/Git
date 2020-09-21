# 10_whileTest01.py

# 숫자 5를 입력 받고 5단 출력 하기
# 5*1 = 5
# 5*2 = 10
# 음수가 들어 오면 절대값으로 변경하여 출력하기

dan = int(input("n 단 출력 : "))
abs(dan)

i = 1

while i <= 9 :
    aaa = dan * i
    print("%d * %d = %d" % (dan, i, aaa))
    i += 1

print("finished")
print("-" * 30)

# 이뒤로 똥사라가서 못들음