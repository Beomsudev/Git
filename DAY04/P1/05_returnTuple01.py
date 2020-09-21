# 05_returnTuple01.py

#튜플을 사용하여 반환되는 데이터를 여러개 만들기

def myfunc(su1, su2):
    if su2 == 0:
        temp = su1
    else:
        temp = su1 // su2
    return su1 + su2, su1-su2, su1*su2, temp


su1 = 14
su2 = 2
result = myfunc(su1, su2)
print(result)
print("-" * 30)

# 문제
# 리스트의 모든 요소의 절대값을 구하고 아래 목록을 튜플로 반환
# 출력 결과 : (가장 큰수, 가장 작은수, 총합, 평균)

def myfunc02(data):
    data_abs = ()

    for a in data:
        if a < 0:
            a = -a
        else :
            a = a

        data_abs += (a,)

    return max(data_abs), min(data_abs), suㄴm(data_abs), (sum(data_abs) / len(data_abs))

mylist = [10, 20, -30, -40, 50]
print(myfunc02(mylist))
print("-" * 30)


# 내 답이랑 선생님 답이랑 비교 해보기 !