# 01_bs4Exam.py

from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding='utf-8')

soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
print("-" * 30)

body = soup.select_one('body')
ptag = body.find('p')




# 읽기
# print(body)
# print("-" * 30)
# print(type(body))
# print(ptag)
# print("-" * 30)
# print(ptag['class'])
# print(ptag['align'])
# print("-" * 30)
# print(type(ptag['align']))
# print("-" * 30)

print("-" * 30)

# 쓰기
ptag['id'] = 'apple'
print(ptag['id'])
print(ptag)
print("-" * 30)

body_tag = soup.find('body')
print(body_tag)
print("-" * 30)

print(type(body_tag))
print("-" * 30)
print(body_tag)
print("-" * 30)
idx = 0
# white character :
for child in body_tag.children:
    idx += 1
    print(str(idx) + '번째 요소 : ', child)
    print('#' * 20)
print("-" * 30)

# mydiv = soup.find('div')
# print(mydiv)
# print("-" * 30)
# print('나의 부모는')
# print(mydiv.parent)
# print("-" * 30)
#
# # attrs 매개 변수는 속성(attribute)을 이용하여 찾고자 할 때 사용
# mytag = soup.find('p', attrs={'class':'hard'})
# print(mytag)
# print("-" * 30)
#
# print(mytag.find_parent())
# print("-" * 30)
#
# print('mytag 태그 모든 상위 부모 태그들의 이름')
# parents = mytag.find_parents()
# for p in parents:
#     print(p.name)