# 10_ramdomDice.py

# 주사위를 10번 던져서 나온 눈의 총합을 구해주는 jusawee 함수를 만드시오
# 단, 시도 횟수가 입력 되지 않으면 5번을 던진다.
def jusawee(su=5):
    import random
    total = 0
    sido_list = []
    for aaa in range(1, su+1):
        su_jusawee = random.randint(1, 7)
        sido_list.append(su_jusawee)
        total += su_jusawee

    print(sido_list)

    return total

sido = 10
print(jusawee(sido))