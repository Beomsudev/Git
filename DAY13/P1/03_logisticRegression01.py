# 03_logisticRegression01.py

import pandas as pd
from sklearn.model_selection import train_test_split

import seaborn as sns

filename = 'iris.csv'
data = pd.read_csv(filename)

# print(data.shape)
# print('-'*30)
#
# print(data.columns)
# print('-'*30)



x_data = [['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y_data = ['Name']
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3)

# 데이터 속성들의 값의 차이가 너무 크면 학습이 잘 안됩니다.
# StandardScaler 클래스를 사용하여 평균 0, 표준 편자 1인 표준정규 분포로 표준화를 수행 합니다.

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
print('train 정확도 : %.3f' % (train_score))

test_score = model.score(x_test, y_test)
print('test 정확도 : %.3f' % (test_score))

print('회귀 계수')
print(model.coef_)
print(model.intercept_)

'''
엑셀 파일을 이용하여 데이터를 읽습니다.
학습용 데이터와 훈련용 데이터를 7:3으로 나눕니다.
데이터를 정규화 합니다.(StandardScaler 클래스)


'''


print('finished')