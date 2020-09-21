# 01_for_practice.py

# 문제 1: 1부터 10까지의 정수중에서 짝수의 총합과 홀수의 총합을 각각 구해 보세요.


# even = 0
# odd = 0
# for aaa in range(1,11):
#     if aaa%2 == 0:
#         even += aaa
#     else:
#         odd += aaa
#     aaa += aaa
#
# print("홀수 합 {}, 짝수 합 {}".format(odd, even))

# 문제 1 : 정답!

# 문제 2 : 1부터 50까지의 정수중에서 3의 배수가 아닌 수
# sumA = 1 + 2 + 4 + 5 + ... + 50
# sumB = 3 + 6 + 9 + ... + 48
# sumA - sumB = 459

# 1 내 방법으로 풀기
# aaa = 0
# bbb = 0
# for idx in range(1, 51):
#     if idx % 3 == 0:
#         aaa += idx
#     bbb += idx
#     idx += 1
#
# result = bbb - aaa
# print(result)

# 2 선생님 방법
# sumA = sumB = 0
# for idx in range(1, 51):
#     if idx % 3 == 0 :
#         sumB += idx
#     else:
#         sumA += idx
#     aaa = sumA - sumB
#
# print(aaa)

# mylist = []
# for idx in range(3, 51, 3):
#     mylist.append(idx)
#     idx += 3
# mylist2 = []
# for idx in range(1, 51):
#     mylist2.append(idx)
#     idx += 1
#
# print(sum(mylist))
# print(sum(mylist2))
# sum1 = sum(mylist)
# sum2 = sum(mylist2)
# print(sum2-sum1)

# 점수가 60이상이면 합격, 그렇지 않으면 불합격
#
# examdata = [90, 30, 65, 45, 80]
# print(examdata)
# print("-" * 30)
#
# for idx in examdata:
#     if idx >= 60:
#         continue
#     else:
#         print("불합격")

# 문자열 다루기
# 아래 문장을 짝수 list는 대문자, 홀수 list는 소문자 각 단어 연결은 "#"으로 처리 하시오
# mystring = "python is very easy"
# mylist = mystring.split()
#
# for idx in range(len(mylist)):
#     if idx % 2 == 0:
#         mylist[idx] = mylist[idx].upper()
#     else:
#         mylist[idx] = mylist[idx].lower()
#
# result = ("#").join(mylist)
# print(result)

# tuple을 for로 다루기
#            00  01    10  11    20  21
# examdata = [(50, 70), (60, 75), (55, 80)]
#
# for midexam, finalexam in examdata:
#     print("중간 고사 {}, 기말 고사 {}".format(midexam, finalexam))
#
# # 고사별 총합을 구하시오
#
# mid_sum = final_sum = 0
# for midexam, finalexam in examdata:
#     mid_sum += midexam
#     final_sum += finalexam
#
# print(mid_sum, final_sum)
#
# mid_sum = final_sum = 0
# # range 함수를 사용하여 고사별 총합을 구하시오
# for idx in range(len(examdata)):
#     mid_sum += examdata[idx][0]
#     final_sum += examdata[idx][1]
#
# print(mid_sum, final_sum)
#
# mylist01 = [idx for idx in range(1, 5)]
# print(mylist01)
#
# mylist02 = [2 * idx for idx in range(1, 5)]
# print(mylist02)
#
# mylist03 = [idx for idx in range(1, 101, 3)]
# print(mylist03)
#
# mylist04 = [idx for idx in range(1, 101, 3) if idx % 10 == 0]
# print(mylist04)
#
# # 1 부터 10까지의 정수 중 3의 배수가 아닌 수들의 합을 list comprehension으로 만드시오
# mylist05 = [idx for idx in range(1, 11) if idx % 3 != 0]
# print(mylist05)
#
# # 중첩 for 1
# mylist06 = [x * y for x in range(2, 10) for y in range(1, 10)]
# print(mylist06)
#
# mylist = [("김", 10), ("이", 20), ("최", 30)]
# mydict = {data[0]:data[1] for data in mylist}
# print(mydict)
#
# # 문제 : students를 list 사용 하여 다음과 같은 dict을 만드시오
# # "이순신":(80, 90), "김유신":(70, 40)]
# students = [("이순신", 80, 90), ("김유신", 70, 40)]
#
# mydict = {data[0]:data[1:3] for data in students}
# print(mydict)

# 문제 정수 2개를 입력 받아서, 앞수에서 뒤수 사이에 있는 모든 정수의 합을 구하시오
# num1 = int(input("입력 1 : "))
# num2 = int(input("입력 2 : "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# total = 0
# for idx in range(num1 + 1, num2):
#     total += idx
#
#
#
# print("합은 %d 입니다." %(total))
#
# kim = ["김유신", 10, 20, 1]
# lee = ["이순신", 30, 40, 1]
# park = ["박영희", 60, 50, 1]
# student = [kim, lee, park]
#
# print(student)
# print("-" * 30)
#
# mylist = list()
#
# for sublist in student :
#     print(sublist)
#     mylist.append((sublist[0], sublist[1], sublist[2]))
#
# print(mylist)

# for 사전 활용
# fruits = [("바나나", 10), ("수박", 20), ("오랜지", 30)]
#
# mydict = {}
#
#
# for key, value in fruits:
#     mydict[key] = value
#
# print(mydict)
# print("-" * 30)
# mydict.clear()
#
# fruits = [("바나나", 10), ("수박", 20), ("오랜지", 30), ("바나나", 50)]
#
# for key, value in fruits:
#     if not (key in mydict):
#         mydict[key] = value
#     else:
#         aaaa = mydict[key]
#         mydict[key] = aaaa + value
#
#
#
# print(mydict)

# nestedDict

# [('sale 무로 배송 할인', '스팸'), ('일정 변경', '일반'), ('sale 변경', '일반')]
# ------------------------------
# words 집합 :  {'변경', '일정', '배송', '할인', 'sale', '무로'}                                        key의 단어 dict
# 카테고리 : 사전 :                                                                                   value의 단어 갯수 dict
# {'스팸': 1, '일반': 2}
# 워드 : 사전 :                                                                                     각 밸류안의 단어 갯수 dict
# {'스팸': {'sale': 1, '무로': 1, '배송': 1, '할인': 1}, '일반': {'일정': 1, '변경': 2, 'sale': 1}}

mylist = [("sale 무로 배송 할인", "스팸"), ("일정 변경", "일반"), ("sale 변경", "일반")]
print(mylist)
print("-" * 30)

words = set()   # 단어들을 저장할 집합


word_dict = {}     # 카테고리별 각 단어들의 빈도수를 저장할 중첩 사전
category_dict = {} # 카테고리별 빈도수를 저장할 사전

for email, cate in mylist:
    if cate in category_dict:
        category_dict[cate] += 1
    else:
        category_dict[cate] = 1

    result = email.split()
    for one in result:
        words.add(one)

    if not cate in word_dict:
        word_dict[cate] = {}

    for one in result :
        if one in word_dict[cate]:
            word_dict[cate][one] += 1
        else:
            word_dict[cate][one] = 1
