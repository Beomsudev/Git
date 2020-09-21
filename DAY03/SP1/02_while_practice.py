# 02_while_practice.py

# 문제 1 : 1 부터 10까지의 총합 구하기

# total = 0
# i = 1
# while i <= 10:
#     total += i
#     i += 1
#
# print(total)

# 문제 2 : 1+3+5 ....97+99 = 2500 (1~100 사이의 홀수의 합)
#
# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 2
# print(total)

# 문제 3 : 숫자 n을 입력 받고 n단 출력 하기
#
# dan = 3
# i = 1
# while i <= 9:
#     print(dan*i)
#     i += 1
#
# cnt = 0
# while True:
#     print("a" + str(cnt))
#     cnt += 1
#     if cnt == 5:
#         break

# 사용자가 입력한 시험 점수에 대한 평균과 개수를 구하시오
# 음수 값이 입력되면 프로그램은 종료
#
# count = 0
# total = 0
# average = 0
# while True:
#     jumsu = int(input("점수 입력 : "))
#     if jumsu > 0:
#         count += 1
#         total += jumsu
#         average = total/count
#     else:
#         break
#
#
# print('총 시험 횟수 : {}'.format(count))
# print('총점 : {}'.format(total))
# print('평균 : %.3f' % (average))
#
# print('finished')

# 랜덤한 1~100의 숫자를 n번만에 사람이 입력하여 맞추는 게임을 작성하시오
import random
count = 0
total = 0
answer = random.randint(1, 100)
print(answer)

while True:
    my_answer = int(input("입력 : "))
    count += 1
    if my_answer == answer:
        print("정답 입니다! %d번 만에 맞췄습니다." %(count))
        break
    elif my_answer > answer:
        print("up")
    elif my_answer < answer:
        print("down")

