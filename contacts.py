class Contact:
    def _init__(self, name , phone, email, addr):
        self.name = name    # self.name과 name은 서로 다른 존재 , 할당함으로써 연결됨
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print(f'이름: {self.name}, 전화번호 {self.phone}, 이메일: {self.email}, 주소: {self.addr}')
        # self.name과 name은 서로 다른 존재 이므로{self.name} 과 {name} 은 서로 다른 상태이다.
        
    @staticmethod
    def set_contact():
        name = input('이름') # 나머지 완성
        phone = input('전화번호') 
        email = input('이메일') 
        addr = input('주소') 

        contact = Contact(name, phone, email, addr) # Contact는 클래스명, contact는 인스턴스명 / 대소문자로 구분해 주는 것 권장
        return contact
    
    @staticmethod
    def get_contact(clist):
        for i in clist:
            i.print_info()  # 8번라인에 선언된 메소드(클래스 내부에 선언된 함수)

    @staticmethod
    def del_contact(clist, name):
        for i,t in enumerate(clist):    # i = index, t = 요소(인스턴스)를 출력한다 의 의미
            if t.name == name:
                del clist[i]

    @staticmethod
    def print_menu():
        print('1 연락처 입력')    
        print('2 연락처 출력')
        print('3 연락처 삭제')
        print('4 종료')
        menu = input('메뉴선택:')
        return menu

    @staticmethod
    def run():
        clist =[]    
        while 1:
            menu = Contact.print_menu()
            if menu =='1':
                t =Contact.set_contact()
                clist.append(t)

            if menu =='2':
                t =Contact.get_contact(clist)
                clist.append(t)       

            if menu == '3':
                t =Contact.del_contact(clist)
                clist.append(t)
                
            elif menu =='4':
                break

if __name__ == '__main__':
    Contact.run()


# """
# python의 데코레이터는 함수형 2가지, class형 2가지 총 4가지 방식을 통해 작성할 수 있습니다.
# 1. 함수형 decorator(데코레이터에 인수 전달이 없는 경우 X)
# 1) main 함수 제작(Decorator함수에 끌려갈 함수)
# 2) Decorator 함수에 전달받을 함수 받기 & Decorator 함수 안에 main 함수를 매개변수로 갖는 함수 제작(wrapper라고 주로 부름)
# 3) wrapper에서 전달받은 main 함수를 호출 or return(사용자 마음대로)
# 4) Decorator함수(wrapper 함수와 같은 위치)에서 wrapper를 return
# 2. 함수형 decorator(데코레이터에 인수 전달이 있는 경우 O)
# 1) main 함수 제작(Decorator함수를 먼저 작성해도 상관 없음.)
# 2) Decorator 함수 제작 인수 전달이 있는 경우엔 main 함수가 아니라 decorator의 매개변수를 먼저 불러옴.(decortator의 변수 지정)
# 3) decorator 안에 진짜 데코레이터(1.의 구조와같음) 구현 real_deco에서 main함수를 매개변수로 전달받는다.
# 4) real_deco의 안에 wrapper 생성(wrapper에서 function(main)의 매개변수를 받음.
# 5) real_deco에서 wrapper를 반환하고 가장 바깥의 main_deco에서 real_deco를 리턴한다.
# 3. Class 형 decorator(데코레이터에 인수가 없는 경우 X)
# 1) __init__메서드에 main함수(호출할 함수) 저장, self.function = function
# 2) __call__(인스턴스를 함수 호출처럼 사용가능하게 만들어줌.)메서드에 호출할 함수의 매개변수를 넘긴다.
# 3) 메인함수에 매개변수를 넣어서 호출하는 형태로 return
# 4. Class 형 decorator(데코레이터에 인수가 있는 경우 O)
# 1) __init__메서드에 decorator의 인수 저장
# 2) __call__ 메서드에 호출할 함수를 전달한다.
# 3) 메인함수에 매개변수를 넣어서 호출하는 형태로 return
# 4) __call__메서드에 wrapper 함수 생성 후 wrapper에 매개변수 전달
# 5) wrapper 함수에서 전달받은 함수 return6) __call__ 메서드의 리턴을 return wrapper(매개변수)과 같은 형식으로 한다.
# """

