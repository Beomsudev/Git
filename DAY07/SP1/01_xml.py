# 01_xml

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import parse


#
# human = Element('human')
# human.attrib['birth'] = '19701225'
# human.attrib['gender'] = '남자'
#
# SubElement(human, 'name').text = '홍길동'
# SubElement(human, 'age').text = '30'
# SubElement(human, 'address').text = '용산구 도원동'
#
# def indent(elem, level = 0):
#     mytab = '\t'
#     i = '\n' + level * mytab
#
#     if len(elem) :
#         if not elem.text or not elem.text.strip() :
#             elem.text = i + mytab
#
#         if not elem.tail or not elem.tail.strip() :
#             elem.tail = i
#
#         for elem in elem :
#             indent(elem, level + 1)
#
#         if not elem.tail or not elem.tail.strip() :
#             elem.tail = i
#     else :
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail = i
#
# indent(human)
#
# xmlFile = 'xmlEx_01.xml'
# ElementTree(human).write(xmlFile, encoding='utf-8')
#
# print(xmlFile + '  파일이 생성되었습니다.')
#
#
# mydict = {'kim':('김철수', 30, '남자', '강남구 역삼동'), 'park':('박영희', 40, '여자', '서초구 방배동')}
# print(mydict.items())
# a = mydict.items()
#
# members = Element('members')
#
# for key, mytuple in mydict.items():
#     myattrib = {'a':'b', 'c':'d'}
#     mem = SubElement(members, 'member', attrib=myattrib)
#     mem.attrib['id'] = key
#
#     SubElement(mem, 'name').text = mytuple[0]
#     SubElement(mem, 'age').text = str(mytuple[1])
#     SubElement(mem, 'gender').text = mytuple[2]
#     SubElement(mem, 'address').text = mytuple[3]
#
# def indent(elem, level = 0):
#     mytab = '\t'
#     i = '\n' + level * mytab
#
#     if len(elem) :
#         if not elem.text or not elem.text.strip() :
#             elem.text = i + mytab
#
#         if not elem.tail or not elem.tail.strip() :
#             elem.tail = i
#
#         for elem in elem :
#             indent(elem, level + 1)
#
#         if not elem.tail or not elem.tail.strip() :
#             elem.tail = i
#     else :
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail = i
#
# indent(members)
#
# xmlFile = 'xmlEx_02.xml'
#
# ElementTree(members).write(xmlFile, encoding='utf-8')

tree = parse('xmlEx_03.xml')
myroot = tree.getroot()
print(type(myroot))
print('-' * 30)

print(myroot)
print('-' * 30)

# 해당 속성들의 키를 list 형식으로 반환
print(myroot.keys())
print('-' * 30)

# 해당 속성들의 키와 값을 튜플로 가지는 list를 반환
print(myroot.items())
print('-' * 30)

print(myroot.get('설명'))
print('-' * 30)

print(myroot.get('qwert', '없을 경우 기본 값'))
print('-' * 30)

print(myroot.findall('가족'))
print('-' * 30)

family = myroot.find('가족')
print(family)
print('-' * 30)

# childs = family.getchildren()
# print(childs)
childs = [item for item in family]
print(childs)
print('-' * 30)

for onesaram in childs :
    # print(onesaram)
    # print('#' * 30)
    elem = [item for item in onesaram]
    for abc in elem:
        print(abc.text)
        if abc.text == '이순자':
            print(abc.attrib['정보'])

    print('^' * 30)

allfamily = myroot.findall('가족')
for onefamily in allfamily:
    # print(onefamily)
    # families = [item for item in onefamily]
    # print(families)
    # print('%' * 30)
    for onesaram in onefamily:
        name = onesaram.find('이름')
        if name != None :
            print(name.text)
        else :
            print(onesaram.attrib['이름'])

print('%' * 30)
