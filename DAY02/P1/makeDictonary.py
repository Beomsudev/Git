# makeDictonary.py
# 관련 함수 : keys(), values()

mydict = {"김철수":35, "박영희":50, "홍길동":40}
print(mydict)

print("-" * 30)

# fot 단수의이름 in 복수:
for key in mydict.keys() :
    print(key)

print("-" * 30)

for value in mydict.values() :
    print(value)

print("-" * 30)

for key in mydict.keys() :
    print("{}의 나이는 {}입니다." .format(key, mydict[key]))

print("-" * 30)

for key, value in mydict.items():
    print("{}의 나이는 {}입니다." .format(key, value))

print("-" * 30)

findkey = "심형래"
if findkey in mydict :
    print(findkey + "은 존재함")
else :
    print(findkey + "은 존재 안 함.")

print(mydict)
result = mydict.pop("홍길동")
print("pop 이후 내용 : ", mydict)
print("pop 된 내용 : ", result)