# 02_Io.py

# 폴더 만들기

myfile01 = open(file='newfile.txt', mode='w', encoding='utf-8')

for idx in range(1, 11):
    data = '%2d번째 줄입니다.\n' %(idx)
    myfile01.write(data)

myfile01.close()

myfile02 = open(file='newfile.txt', mode='a', encoding='utf-8')

for idx in range(11, 101):
    data = '%3d번째 줄입니다.\n' % (idx)
    myfile02.write(data)

myfile02.close()

for idx in range(1, 11):
    filename = 'somefile' + str(idx).zfill(2) + '.txt'
    myfile = open(file=filename, mode='w', encoding='utf-8')
    data = '메롱' + str(idx).zfill(5)
    myfile.write(data)
    myfile.close()

print('-'* 20)
with open(file='test.txt', mode='w', encoding='utf-8') as myfile:
    myfile.write('메롱\n')
    myfile.write('하하\n')
    print('가나다라', file=myfile)

with open(file='test.txt', mode='r', encoding='utf-8') as myfile:
    # print(myfile.read())
    # print(type(myfile.read()))
    print(myfile.readlines())