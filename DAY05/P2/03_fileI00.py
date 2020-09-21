# 03_fileIo0.py

# 파일 입출력
# open() 텍스트/바이너리 파일을 읽거나 쓰기위한 함수
# open(file='전체경로 + 파일이름', mode='r/w/a', mode='t/b', encoding='utf-8')
# mode : r(read_기본값) / w(write) / a(append), t(text_기본값) / b(binary)

# encoding : 인코딩 문자열'utf-8', 'utf-16' (일반적으로 utf-8 사용
myfile01 = open(file='newfile.txt', mode='w', encoding='utf-8')

for idx in range(1, 11):
    data = '%2d 번째 줄입니다.\n' %(idx)
    myfile01.write(data)

myfile01.close()

myfile02 = open(file='newfile.txt', mode='a', encoding='utf-8')

for idx in range(11, 101):
    data = '%3d 번째 줄입니다.\n' %(idx)
    myfile02.write(data)

myfile02.close()

print('여러개의 파일 만들기')
for idx in range(1, 10):
    filename = 'somefile' + str(idx).zfill(2) + '.txt'
    myfile = open(file=filename, mode='w', encoding='utf-8')
    data = '메롱' + str(idx).zfill(5)
    myfile.write(data)
    myfile.close()

print('with 구문 사용하기') # with 구문으로 파일 만들기
# with 구문은 암시적으로 close를 수행해 줌
# 따라서, close() 함수를 사용하지 않아도 됨

with open(file='test.txt', mode='w', encoding='utf-8') as myfile :
    myfile.write('메롱\n')
    myfile.write('하하\n')
    print('가나다라', file=myfile) # print('가나다라') > myfile에 추가됨
    # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    # 원래는 sys.stdout(내가보고 있는 모니터)로 출력되는데 이걸 file=myfile로 변경 했기 때문

print("-"  * 30)

with open(file='test.txt', mode='r', encoding='utf-8') as myfile :
    # print(myfile.read())              # str로 불러옴
    # print(type(myfile.read()))
    print(myfile.readlines())           # list로 불러옴
    print(type(myfile.readlines()))

print('finished')

