from bs4 import BeautifulSoup
from urllib.request import urlopen
# 타이틀번호, 요일, 제목, 링크 로 csv파일 만들기
# 각 요일별 폴더에 스크린샷 제목이름으로 저장하기

import os,shutil
myfolder = ('d:\\naver_cartoon\\')

weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}

def saveFile(mysrc, weekday, mytitle):
    image_open = urlopen(mysrc)
    # ex) D:\naver_cartoon\월요일
    filename = myfolder + weekday_dict[weekday] + '\\' + mytitle + '.jpg'
    myfile = open(filename, mode='wb')
    myfile.write(image_open.read())
    myfile.close()

try:
    if not os.path.exists(myfolder):
        os.mkdir(myfolder)

    for mydir in weekday_dict.values():
        mypath = myfolder + mydir

        if os.path.exists(mypath):
            shutil.rmtree(mypath)

        os.mkdir(mypath)

except FileExistsError as err :
    print(err)

myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)
print(type(soup))
print('-'*30)
# print(soup)

mytarget = soup.find_all('div', attrs={'class':'thumb'})
print(len(mytarget))
# print(mytarget)

mylist = []

for abc in mytarget:
    myhref = abc.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list.nhn?', '')
    myhref = myhref.split('&')
    titleid = myhref[0].split('=')[1]
    weekday = myhref[1].split('=')[1]
    mysrc = abc.find('img').attrs['src']
    mytitle = abc.find('img').attrs['title']

    saveFile(mysrc, weekday, mytitle)

    sublist = []
    sublist.append(titleid)
    sublist.append(mytitle)
    sublist.append(weekday)
    sublist.append(mysrc)
    mylist.append(sublist)


    # mylist.append(titleid)
    # mylist.append(weekday)
    # print(mylist)


from pandas import DataFrame

mycolumns = ['titleid', 'title', 'weekday', 'src']
myframe = DataFrame(mylist, columns=mycolumns)

filename='cartoon_01.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
print(filename + '저장됨')

print('finished')