# 09_DataFrameExam01.py
#
# from pandas import DataFrame
#
# sdata = {
#     '도시':['서울', '서울', '서울', '부산', '부산'],
#     'year':[2000, 2001, 2002, 2001, 2000],
#     'pop':[1.5, 1.7, 3.6, 2.4, 2.9]
#     }
#
# myindex = ['one', 'two', 'three', 'four', 'five']
# myframe = DataFrame(sdata, index=myindex)
# print(myframe)
# print(type(myframe))
# print('-' * 30)
#
# myframe.index.name = '호호호'
#
# print(myframe.index)
# print('-' * 30)
#
# myframe.columns.name = '하하하'
#
# print(myframe.columns)
# print('-' * 30)
#
# print(myframe.values)
# print(type(myframe.values))     # <class 'numpy.ndarray'>
# print('-' * 30)
#
# print(myframe.dtypes)   # 각 데이터 유형 보기
# print('-' * 30)
#
# print(myframe.T)        # 행, 열 전치함
# print('-' * 30)
#
# print(myframe)
# print('-' * 30)
#
# mycolumns = ['pop', '도시', 'year']
# newframe = DataFrame(sdata, columns=mycolumns)
# print(newframe)
# print('-' * 30)
#
# print('finished')

# dataframeReaderWriter01.py
import numpy as np
from pandas import DataFrame

mylist = [10*onedata for onedata in range(1, 26)]

print(mylist)
print('-'*30)

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군']
mycolumns = ['서울', '부산', '광주', '목포', '경주']
myframe = DataFrame(np.reshape(mylist, (5, 5)) , index=myindex, columns=mycolumns)

# iloc : i는 정수(행 인덱스), loc는 location
result = myframe.iloc[[1]]
print(type(result))
print(result)
print('-'*30)

result = myframe.iloc[[1, 3]]
print(result)
print('-'*30)

# 숫자 색인을 이용하여 짝수행만 출력
result = myframe.iloc[0::2]
print(result)
print('-'*30)

# loc : loc는 location
result = myframe.loc[['이순신']]
# result = myframe.loc['이순신']
print(result)
print('-'*30)

# 이순신과 강감찬 출력
result = myframe.loc[['이순신', '강감찬']]
print(result)
print('-'*30)

result = myframe.loc[['강감찬'], ['광주']]
print(result)
print('-'*30)

# 연산군과 광해군의  광주/목포 출력
result = myframe.loc[['연산군', '광해군'], ['광주', '목포']]
print(result)
print('-'*30)

result = myframe.loc['김유신':'광해군', '광주':'목포']
print(result)
print('-'*30)


result = myframe.loc[[False, True, True, False, True]]
print(result)
print('-'*30)

print(myframe['부산'] <= 100)
print('-'*30)

result = myframe.loc[myframe['부산'] <= 100]
print(result)
print('-'*30)

# 목포의 값이 140인 항목 조회 하기
result = myframe.loc[myframe['목포'] == 140]
print(result)
print('-'*30)

# all()와 any() 함수를 사용하는 예시
# 부산이 70이상이고, 목포가 140이상인 항목들
# 부산이 70이상이거나, 목포가 140이상인 항목들
cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140
print(cond1)
print('-'*30)

print(cond2)
print('-'*30)

df = DataFrame([cond1, cond2])
print(df)
print('-'*30)

print(df.all())
print('-'*30)

print(df.any())
print('-'*30)

result = myframe.loc[df.all()]
print(result)
print('-'*30)

result = myframe.loc[df.any()]
print(result)
print('-'*30)

# lambda 입력매개변수 : 하고자하는 일
aa = lambda x : x + 3
print(aa(10))

result = myframe.loc[lambda df : df['광주'] >= 130]
print(result)
print('-'*30)

myframe.loc[['이순신', '강감찬'], ['부산']] = 30

# 김유신부터 광해군까지, 경주의 실적을 80으로 변경하기
myframe.loc['김유신':'광해군', ['경주']] = 80

myframe.loc[['연산군'], :] = 55

myframe.loc[:, ['광주']] = 60

print(type(myframe))
print(myframe)
print('-'*30)

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

myframe.index.name = '이름'
myframe.columns.name = '점수'

myframe.plot(kind='bar', rot=0, title='차량 유형별 지역 등록 댓수', legend = True)
filename = 'dfRW01.png'
plt.savefig(filename)
print(filename  + '저장됨')


print('finished')







