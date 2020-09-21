# 06_rangeSum.py

# 문제 정수 2개를 입력 받아서, 앞수에서 뒤수 사이에 있는 모든 정수의 합을 구하세요. # 시간내에 못품
# 앞수 : 2, 뒷수 : 4 이면 2+3+4=9 출력
# 앞수 : 5, 뒷수 : 2 이면 5+4+3+2=14 출력

# 출력 예시 : 2부터 4까지의 총합은 9 입니다.
# 만약 절대값 처리가 필요하면 abs 함수 사용
num_f = int(input("앞 수를 입력 하세요"))
num_b = int(input("뒷 수를 입력 하세요"))

if num_f > num_b :
    num_f, num_b = num_b, num_f # 이해 못함
print(num_f, "/", num_b)

total = 0
for idx in range(num_f, num_b + 1) :
    total += idx

print("%d부터 %d까지의 총합 : %d" % (num_f, num_b, total))

