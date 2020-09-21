# seasonTest.py

# 해당 월과 게절을 출력해주는 프로그램 작성
# 입력 : 9
# 9월은 가을입니다.
# 봄(3~5), 여름(6~8), 가을(9~11), 겨울(12~2)

month = int(input("달을 입력하세요."))

if 3 <= month <= 5 :
    print("%d월은 봄입니다." % (month))
elif 6 <= month <= 8 :
    print("%d월은 여름입니다." % (month))
elif 9 <= month <= 11 :
    print("%d월은 가을입니다." % (month))
elif 12 == month or 1<= month <= 2 : # 또는 이렇게 표현 month in [12, 1, 2]
    print("%d월은 겨울입니다." % (month))
else :
    print("어디 사세요?")