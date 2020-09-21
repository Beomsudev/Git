# 08_logicalTest03.py

# 엑셀 파일을 읽습니다.
# 훈련 데이터와 테스트 데이터를 7:3으로 분리 합니다.
# 최종 결과에 대하여 정확도를 구해 봅니다.
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.optimizers import SGD
from sklearn.model_selection import train_test_split
import tensorflow as tf

filename = 'logicalTest03.csv'
data = np.loadtxt(filename, delimiter=',', dtype=np.int32)  # dtype : 타입설정

table_col = data.shape[1]
y_column = 1
x_column = table_col - 1

x = data[:, 0:x_column]
y = data[:, x_column:]

seed = 1
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3''', random_state=seed''')

model = Sequential()

model.add(Dense(units=y_column, input_dim=x_column, activation='sigmoid'))

learning_rate = 0.1
sgd = tf.keras.optimizers.SGD(lr=learning_rate)

model.compile(loss='binary_crossentropy', optimizer=sgd)

model.fit(x=x_train, y=y_train, epochs=2000, verbose=0)

total = 0
hit = 0


for idx in range(len(x_test)):
    result = model.predict_classes(np.array([x_test[idx]]))
    print('테스트 용 데이터 : %s' % x_test[idx])
    print('정답 : %s' % y_test[idx], end='')
    print('예측 값 : %s' % str(result.flatten()))

    total += 1

    # 예측 값과 정답이 같은 경우 1추가
    hit += int(y_test[idx] == result.flatten())        # int(논리식) 논리식이 참이면 1반환, 거짓이면 0반환
    print('-' * 30)
# end for

accuracy = hit / total # 정확도
print('정확도는 %.4f' % accuracy)

print('finished')



