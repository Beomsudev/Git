# 02_multiLinear03.py

# multiLinear03.csv 파일을 7대 3으로 나누어 선현 회귀 분석을 수행 하세요.
# x_column = 3, y_column = 1


import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

# 출력은 1개, 입력은 n(n>=1) n=1이면 단순 회귀, n>1 다중 회귀

# 엑셀 데이터 로딩
filename = 'multiLinear03.csv'
data = np.loadtxt(filename, delimiter=',')

table_col = data.shape[1]   # 4
y_column = 1
x_column = table_col - 1    # 4 - 1 = 3

# 입력과 출력 데이터 분리
x = data[:, 0:x_column]
y = data[:, x_column:]

# 훈련용 데이터 셋과 테스트 용 데이터 셋 분리
seed = 0
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=seed)

# 모델 생성
model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x_train, y_train, epochs=5000, batch_size=10, verbose=0)

print(model.get_weights())

prediction = model.predict(x_test)

for idx in range(len(y_test)):
    label = y_test[idx]     # label = 정답
    pred = prediction[idx]

    print('real : %f, prediction : %f' % (label, pred))


print('finished')

