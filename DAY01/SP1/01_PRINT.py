# 01_PRINT.py
#            0123456
ex_string = "bBeom Se"
ex_list = [1, 2, 3]
ex_tuple = (1, 2, 3)
ex_dict = {"a":1, "b":2, "c":3}
"""
print(ex_string)
print("Beom Su")
print(len(ex_string))
print(len("Beom Su"))
print(len([1,2,3]))
print(len((1,2)))
print(len({"a":1, "b":2}))

print("abcde".find("b"))
print(ex_string.find("B"))
print(ex_string.find("S", 4))
print(ex_string.rfind("e"))
print(ex_string.rfind("e", ))

print(ex_string.replace("B", "T", 0))

print(ex_string.strip())
print(ex_string.lstrip())
print(ex_string.rstrip())

print(ex_string.upper())
print(ex_string.lower())
print(ex_string.capitalize())

ex_string = "abc@def"
print(ex_string.split("@"))

ex_string = "abc.ppt"
print(ex_string.startswith("a"))
print(ex_string.endswith(".ppt"))
print(ex_string.upper().startswith("b"))

print("abcde".upper().startswith("A"))

mylist = ["삼성", "엘지", "sk"]
print("".join(mylist))
aaa = ("a", "a")
print("/".join("aaa"))
print("/".join(("a", "a")))
print("/".join(["a","a","a"]))

bbb = {"a":1, "a":2, "c":3}
print("/".join(bbb))
print("/".join({"a":1, "a":2, "b":3}))

ex_string = "Abc1"
print("aAa"[1].isupper())

#abcdefghijklmnopqrstuvwxyz
munja = "r"
print(munja[0] > "a") # 문자는 r로 인덱싱 상태(korea에서 2로인덱싱)

#복습 필!!!!!
print(munja >= "A" and munja <="Z")
print(munja >= "a" and munja <="z")
print(munja >= "0" and munja <="9")
print(ord(munja))
print(ord("2"))
print(ord("a"))
print(ord("a")+ord("a"))
"""

print("안녕하세요", end="ㅂ")
print("반갑습니다")
print("안녕하세요", "반갑습니다", sep="")
