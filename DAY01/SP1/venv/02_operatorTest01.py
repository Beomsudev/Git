# 02_operatorTest01.py

a = 14
b = 5

# 산술 연산자 : + - * / // % **
sum = a + b
sub = a - b
multiply = a * b
divide = a / b
divide2 = int(a // b)
remainder = a % b
power = 2 ** 10

print('제곱수1: [%d]' % (power))

# 양의 정수는 우측 정렬
# 정수는 확보할 자리수
print('제곱수2: [%3d]' % (power))
print('제곱수3: [%6d]' % (power))
print('제곱수4: [%-6d]' % (power))

su = 12.3456780
print('서식1 : %f' % (su))
print('서식2 : %.2f' % (su))
print('서식3 : %6.2f' % (su))
print('서식4 : %-6.2f' % (su))

