# 12_updownTest.py

# import : 모듈을 사용하고자 할 떄 import 키워드 사용
# random 모듈 : 랜덤한 데이터를 추출 할 때 사용 하는 모듈!


# import random
# for idx in range(1, 11):
#     answer = random.randint(1, 100);
#     print(answer)

import random
answer = random.randint(1, 100);
print(answer)

count = 0


while True:
    su = int(input("1~100 사이의 정수 1개 입력 : "))
    count += 1
    if answer > su :
        print("큽니다.")
#       count += 1 # 나는 여기 적었는데 위에 적는게 정석
    elif answer < su :
        print("작습니다.")
    elif answer == su :
        print("정답! %d번 만에 맞췄습니다." % (count))
        break


# 했갈린 부분 random이 wihile 밖에 있으므로 1번 정해지면 프로그램 끝날때까지 고정임!

print("finished")