# 02_abs01.py

# 어떠한 숫자에 대하여 절대 값으로 만들어 주는 함수 만들기

def absolute(n):
    if n < 0:
        n = -n
    return n

su = -5
a = absolute(su)
print(a)

mylist = [2, -4, -7]
mylist_absolute = []

# 내 답
# for idx in mylist:
#     bbb = absolute(idx)
#     mylist_absolute.append(bbb)
# print(mylist_absolute)

# 선생님 답
res = [absolute(item) for item in mylist]
print(res)

