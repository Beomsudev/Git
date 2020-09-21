# numberTest.py

a = 14
b = 5

sum = a + b
sub = a - b
multiply = a * b
divide = a / b
divide2 = int(a // b) # 이 부분 이해 못함 !
remainder = a % b
power = 2 ** 10

print("덧셈 : %d" %(sum))
print("뺄셈 : %d" %(sub))
print("곱셈 : %d" %(multiply))
print("나눗셈 : %f" %(divide))
print("나눗셈2 : %d" %(divide2))
print("나머지 : %f" %(remainder))
print("제곱수 : %d" %(power))

# 양의 정수는 우측 정력
# 정수는 확보할 자리수
print("제곱수2 : [%3d]" %(power))  #power는 4자릿수인데 3자리라서 무시됨
print("제곱수3 : [%6d]" %(power))  #왼쪽부터 6자리해서 남는 2자리 공백
print("제곱수4 : [%-6d]" %(power)) #오른쪽부터 6자리해서 남는 2자리 공백

su = 12.3456789
print("서식1 : [%f]" % (su))
print("서식2 : [%.2f]" % (su))
print("서식3 : [%6.2f]" % (su)) # 6 = 전체 6자리이고, 소수점은 2자리만 표현(소수점 포함 6자리이하)
print("서식4 : [%-6.2f]" % (su))
