# 02_tuple_p.py

tuple1 = (1, 2, 3, 4, "a", "b", "c")
tuple2 = (1, 2, 3, 4)
tuple3 = ("abc", "def")
tuple4 = ()
tuple5 = tuple()
aaa = tuple1 + ("a",)
print(aaa)

bbb = tuple1 * 3
print(bbb)

print(tuple4)
print(tuple5)

tuple6 = 1,2,3,4
print(tuple6)
print(type(tuple6))

a = tuple1[1]
print(a)