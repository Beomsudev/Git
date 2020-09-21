# exam01.py
# 학생의 이름과 국어, 영어, 수학 점수를 입력 받으세요.
# 김철수 : 50, 60, 80
# 총점은 소수 점 2자리로, 평균은 소수점 3자리로 출력하세요.
# 출력 결과
# 이름 : 김철수
# 국 : 50점
# 영 : 60점
# 수 : 80점
# 총점 : 190점
# 평균 : 10110점


# input으로 입력 받으세요.
print("이름을 입력 하세요.")
name = input()
print("국어 점수를 입력 하세요.")
kor = int(input())
print("영어 점수를 입력 하세요.")
eng = int(input())
print("수학 점수를 입력 하세요.")
math = int(input())

total = kor + eng + math
ave = total / 3
print(name, "님의 점수입니다.")
print("국어 : %d점" % (kor))
print("영어 : %d점" % (eng))
print("수학 : %d점" % (math))

print("총점 : %.2f점" % (total))
print("평균 : %.3f점" % (ave))


