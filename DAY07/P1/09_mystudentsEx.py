# 09_mystudentsEx.py

# mystudent.xml 파일을 읽어서 students.csv 파일 만들기
# students.db 파일에 students 테이블을 생성하고, 데이터를 추가하세요
# pandas, DataFrame, sqlite, xml 패키지
# 추가 사항 : 총점과 평균도 같이 csv파일과 db의 테이블에 같이 해보기

from xml.etree.ElementTree import parse

filename = 'mystudent.xml'
tree = parse('mystudent.xml')
myroot = tree.getroot()
print('-' * 30)

students = myroot.findall('student')
#print(students)
print('-' * 30)


student = [item for item in students]
#print(student)
print('-' * 30)

for qqq in student:
    qqq = students.getchildren()
    print(qqq)
    print('-' * 30)

#################################

# tree = parse('mystudent.xml')
# myroot = tree.getroot()
# # print(type(myroot))
#
# allstudents = myroot.findall('student')
# print(allstudents)
#
#
#
# totallist = []  #
# for onesaram in allstudents:
#     print(onesaram)
#     childs = onesaram.getchildren()
#     print(childs)
#     sublist = []
#     for onedata in childs:
#         sublist.append(onedata.text)
# print(sublist)