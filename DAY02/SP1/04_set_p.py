# 04_set_p.py

list01 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]

print(list01)

set01 = set(list01)
print(list01)
print(set01)

print(type(set01))

set01.update([7, 8, 9])
print(set01)

set01.remove(5)
print(set01)

