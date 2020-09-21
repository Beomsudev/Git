# 04_for05.py

# 문자열 for문 으로 다루기

mystring = input("문자열 입력 : ") # python is very easy
mylist = mystring.split()
print(type(mylist))
print(mylist)

print("-" * 30)
for idx in range(len(mylist)) : # idx는 라는 변수는 자동으로 0 지정되 있음
    if idx % 2 == 0 :
        mylist[idx] = mylist[idx].upper()
    else :
        mylist[idx] = mylist[idx].lower()

result = "#".join(mylist)
print(result)