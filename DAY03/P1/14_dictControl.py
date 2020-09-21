# 14_dictControl.py

# 역시 이해 못함 dict, set, list, tuple 개념 확립이 안됨

# 100번 반복한다.
# 매번 1부터 10 사이의 임의의 수를 추출한다.
# 이것을 사전에 담고, 최종 결과를 출력 하도록 한다.
# 출력 결과 예시
# 숫자 1은 12번 추출
# 숫자 2는 5번 추출
# ...
# 숫자 10은 4번 추츨
# ("1":2, "2":4 ... "10":5)

import random

mydict = {} # empty dict == "mydict = dict()"

for idx in range(1, 101) :
    data = random.randint(1, 10)

    if data in mydict :
        mydict[data] += 1
    else :
        mydict[data] = 1

print(mydict)

mylist = [key for key in mydict.keys() ]
mylist.sort()

for key in mylist :
    print("숫자 %d는 %d번 추출" % (key, mydict[key]))

print("finished")

