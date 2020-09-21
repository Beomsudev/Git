# 08_makeDict02.py

# 전체 이해 못함

fruits = [("바나나", 10), ("수박", 20), ("오랜지", 30)]

mydict = dict() # empth dict
print(mydict)
print("-" * 30)

for key, value in fruits : # 이해 못함
    mydict[key] = value

print(mydict)
print("-" * 30)

mydict.clear()

fruits = [("바나나", 10), ("수박", 20), ("오랜지", 30), ("바나나", 50)]

for key, value in fruits : # 이해 못함
    if not key in mydict : # 들어 있지 않으면, 들어 있으면은 not 삭제
        mydict[key] = value
    else :
        aaaa = mydict[key]
        mydict[key] = aaaa + value

print(mydict)
print("-" * 30)