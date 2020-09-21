# 02_class.py

class Calculator : # step1. 클래스 정의
    def __init__(self, data):
        self.result = 0 # 총합을 0값으로 초기화
        self.data = data
        print(self.data + ' 계산기가 생성되었습니다.')
        print('계산기 초기 값 :', self.result)

    def calc(self, num): # 함수는 동작

        self.result += num
        return self.result

cal1 = Calculator('계산기 A')

# step3
print(cal1.calc(3))
print(cal1.calc(4))
print(cal1.calc(4))
a = cal1.calc(5)
print(a)
print('-'*30)

cal2 = Calculator('계산기 B')
print(cal2.calc(5))
print(cal2.calc(15))
b = cal2.calc(6)
print(b)
print('-'*30)

print(a+b)

print('finished')

class Pet:
    def __init__(self, name, sleeptime, feed = '고등어'):
        self.name = name
        self.sleeptime = sleeptime
        self.feed = feed

    def sleep(self):
        remark = self.name + '가(이)' + str(self.sleeptime) + '시간 동안 잠을 잡니다.'
        print(remark)

    def eat(self):
        remark = self.name + '가(이)' + self.feed + '를 먹습니다.'
        print(remark)

romeo = Pet('삽살이', 3, '사료')
romeo.eat()
romeo.sleep()

juliet = Pet('야옹이', 4)
juliet.eat()
juliet.sleep()

print('finished')