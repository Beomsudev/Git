# 03_jsonTest02.py

# 첨부 파일 some.json을 이용하여 각 정보를 출력해보세요.

import json


filename = 'some.json'

def get_Json_Data():
    print('함수 호출됨')
    filename = 'some.json'

    myfile = open(filename, 'rt', encoding='utf-8')
    print(type(myfile))

    myfile = myfile.read()
    print(type(myfile))
    # loads(str) : 문자열 형식의 데이터를 이용하여 json 타입으로 변환해주는 함수입니다.

    jsonData = json.loads(myfile)
    print(type(jsonData))
    print('-' * 30)
    print(jsonData)

    member = jsonData['member']
    web = jsonData['web']
    print(member)
    print(web)
    print('-' * 30)

    name = member['name']
    address = member['address']
    phone = member['phone']
    cafename = web['cafename']
    id = web['id']

    print('멤버 이름 : %s / 주소 : %s / 번호 : %s' % (name, address, phone))
    print('카페 이름 : %s / id : %s' % (cafename, id))

# __name__ : 파이썬이 내장하고 는 내부 변수
# 애플리케이션 이름이 저장되어 있다.
# #해당 애플리케이션이 스스로 실행하면 '__main__' 값이 대입된다.
if __name__ == '__main__':
    print('나 스스로 실행 되었습니다.')
    get_Json_Data() # 함수 호출
else:
    print('다른 프로그램이 호출 했습니다.')