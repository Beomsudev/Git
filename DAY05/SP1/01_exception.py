try:
    a = 3
    print(a)

except ZeroDivisionError as err:
    print("0으로 나누기 불가")
    print(err)

except IndexError as err:
    print("인덱스 범위 초과")
    print(err)

except KeyError as err:
    print("키없다")
    print(err)

except Exception as err:
    print('기타')
    print(err)

else:
    print("예외가 없을 때")

finally:
    print("예외 발생 여부와 상관 없이 실행")