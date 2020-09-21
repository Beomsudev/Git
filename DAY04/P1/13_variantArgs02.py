# 13_variantArgs02.py

# minval : 튜플 요소에서 가장 큰 수와 가장 작은 수를 반환하는 함수를 만드시오
def minval(*args) :
    max01 = max(args)
    min01 = min(args)

    print("max : ", max01)
    print("min : ", min01)

print(minval(3, 5, 8, 2))


def minval02(*args):
    mylist = [ item for item in args]
    mylist.sort()
    return mylist[0], mylist[-1]

print(minval02(3, 5, 8, 2))

