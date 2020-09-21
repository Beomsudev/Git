# 02_mypet.py
# Pet 클래스 : 생성자 구현, 함수 구현(sleep(), eat())

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