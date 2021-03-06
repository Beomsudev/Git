# 03_singleLinear01.py

# 카페에서 '회귀분석예제파일.zip' 파일 받기

import numpy as np

# sklearn : science kit (머신 러닝을 하기 위한 패키지)
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
'''
1. 첨부 엑셀 파일을 읽어 옵니다.
2. 훈련/학습 데이터와 테스트 데이터의 비율을 75대 25로 분리 합니다.
3. 훈련/학습 데이터를 이용하여 선형 회귀 분석을 한 다음, 테스트 데이터를 이용하여 결과를 예측해 봅니다.
 
'''

filename = 'singleLinear01.csv'
data = np.loadtxt(filename, delimiter=',')
print(data)
print(type(data))

table_col = data.shape[1]       # 컬럼 수
y_column = 1                    # 출력(정답) 데이터 컬럼 수
x_column = table_col - y_column # 입력 데이터 컬럼 수

x = data[:, 0:x_column]
y = data[:, x_column:]

print(x)
print('-' * 30)

print(y)
print('-' * 30)

# 입력용학습, 입력용테스트, 출력용학습, 출력용테스트
#                = train_test_split(입력원본, 출력원본, test_size=테스트데이터의 비율)
# 일반적으로 7:3으로 나눔

x_train, x_test, y_train, y_test \
    = train_test_split(x, y, test_size=0.25)

print(x_train)
print('-' * 30)

print(y_train)
print('-' * 30)

# 모델을 생성하고, 학습을 수행 합니다.
# 01 : 모델(작업공간) 생성
model = Sequential()

# 02 : 레이어를 추가합니다.
# Dense : 레이어를 추가하는 사용되는 클래스
# units = 출력값의 크기, input_dim = 입력데이터의 크기, activation = '활성화 함수'
# 'linear' : 선형 회귀 분석
model.add(Dense(units=y_column, input_dim=y_column, activation='linear'))


# 03 : 컴파일을 수행 한다
# loss : 비용(손실) 함수를 지정한다.
# optimizer : 옵티마이저로써, 경사 하강법을 잘 수행하기 위한 가이드
model.compile(loss='mean_squared_error', optimizer='adam')

# 04 : 훈련/학습을 한다.
# epochs : 반복 횟수
# batch_size=1
# verbose : 0(진행 결과를 출력하지 않음), 2(epoch당 1번만 출력), 1(기본값, 한번 테스트마다 출력)
model.fit(x_train, y_train, epochs=5000, batch_size=1, verbose=1)

# 05 : 예측을 한다. 새로운 문제 풀기
prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx] # 정답 데이터
    pred = prediction

    print('real : %f, prediction : %f' % (label, pred))

print(prediction)

print('finished')