# 07_SeriesTest01.py
#
# # Series : 1차원적인 동일한 타입의 데이터 묶음
# # 엑셀 파일의 1개의 컬럼 정보
#
# from pandas import Series
#
# # 색인을 지정하지 않으면, 0 부터 순차적으로 숫자를 매김
# mylist = [10, 20, 30, 40]
# myseries = Series(mylist)
# print(myseries)
# print(type(myseries))
# print('*' * 30)
#
# # 색인을 지정하려면, index 매개 변수를 사용 하면 됨
# myseries = Series(mylist, index=['강감찬', '이순신', '김유신', '광해군'])
# print(myseries)
# print('*' * 30)
#
# # 색인에 이름 지정하기
# myseries.index.name='점수'
# print(myseries)
# print('*' * 30)
#
# # 시리즈 자체에 이름 지정하기
# myseries.name = '학생들 시험'
# print(myseries)
# print('*' * 30)
#
# print(type(myseries))
# print('*' * 30)
#
# # 문자열의 dtype은 'object'입니다.
# print(myseries.index)
# print('*' * 30)
#
#
# print(myseries.values)      # 색인의 값을 출력
# print('*' * 30)
#
# for idx in myseries.index:
#     print('색인 : ' + idx + ', 값 : ' + str(myseries[idx]))

from pandas import Series


myindex = ['서울', '부산', '광주', '대구', '울산', '목포', '여수']
mylist = [50, 60, 40, 80, 70, 30, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-'*30)

print(myseries['대구'])
print(type(myseries['대구']))
print('-'*30)

print(myseries[['대구']])
print(type(myseries[['대구']]))
print('-'*30)

# 문자열 색인으로 슬라이싱하는 경우 양쪽 모두 포함됨.
print(myseries['대구':'목포'])
print('-'*30)

print(myseries[[2]])
print('-'*30)

# 콜론으로 슬라이싱하는 경우에는 대괄호 1개
print(myseries[0:5:2])
print('-'*30)

# 콤마를 사용하는 경우 대괄호 2개
print(myseries[[1, 3, 5]])
print('-'*30)

myseries[2] = 22 # 쓰기
print(myseries)
print('-'*30)

myseries[2:5] = 33
print(myseries)
print('-'*30)

# 서울과 대구만 55로 변경하기
myseries[['서울', '대구']] = 55
print(myseries)
print('-'*30)

myseries[0::2] = 77
print(myseries)
print('-'*30)