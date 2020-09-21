# 01_bs4Exam03.py

import urllib.request

from bs4 import BeautifulSoup
from pandas import DataFrame

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

tags = soup.find_all('div', attrs={'class':'tit3'})         #tags에 대해 정확하게 확인 해보기
print(tags)
print("-" * 30)

for tag in tags :
    print(tag.a.string) #string 속성 : 해당 태그가 가지고 있는 문자열을 출력

print("-" * 30)

print('<a> 태그의 href 전체 태그')
url_header = 'https://movie.naver.com'
for tag in tags:
    print(url_header + tag.a['href'])

print("-" * 30)

mytrs = soup.find_all('tr')
print(len(mytrs))
print("-" * 30)

no = 0 # 순서를 의미하는 번호
totallist = [] # 전체를 저장할 list


for one_tr in mytrs:
    # print(one_tr)
    # print('@' * 30)

    title = ''
    up_down = '' # '상승/항강/불변'을 위한 설명 문구
    mytd = one_tr.find('td', attrs={'class':'title'})

    if mytd != None:
        no += 1
        newno = str(no).zfill(2)

        mytag = mytd.find('div', attrs={'class':'tit3'})
        title = mytag.a.string

        # td 태그 중에서 3번째 요소를 찾기
        mytd = one_tr.select_one('td:nth-of-type(3)')
        myimg = mytd.find('img')
        if myimg.attrs['alt'] == 'up' :
            up_down = '상승'
        elif myimg.attrs['alt'] == 'up' :
            up_down = '강등'
        else:
            up_down = '불변'

        change = one_tr.find('td', attrs={'class':'range ac'})
        change = change.string

        # print(newno + '/' + title + '/' + up_down + '/' + change)

        # totallist.append(()) #안쪽의 소괄호는 tuple
        totallist.append((newno, title, up_down, change))

mycolumn = ['순위', '제목', '변동', '변동값']
myframe = DataFrame(totallist, columns=mycolumn)

filename = 'naverMovie.csv'
myframe.to_csv(filename)


print(filename + '파일 저장 됨')
print("-" * 30)