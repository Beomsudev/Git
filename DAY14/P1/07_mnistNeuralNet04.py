# 07_mnistNeuralNet04.py

from tensorflow.python.keras.datasets import mnist

image_row, image_col, image_dim = 28, 28, 28*28

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape((60000, image_dim))
x_train = x_train.astype('float') / 255.0

x_test = x_test.reshape((10000, image_dim))
x_test = x_test.astype('float') / 255.0

from keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print('y_train[0] : ', y_train[0])


# 모델 생성
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

model = Sequential()

NB_CLASS = 10
HIDDEN_LAYER_1 =512
HIDDEN_LAYER_2 =512
model.add(Dense(units=HIDDEN_LAYER_1, activation='relu', input_shape=(image_dim,)))

model.add(Dense(units=HIDDEN_LAYER_2, activation='relu'))

model.add(Dense(units=NB_CLASS, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

print('model.fit() 중입니다.')
hist = model.fit(x_train, y_train, validation_split=0.3, epochs=5, batch_size=64, verbose=1)

print('히스토리 목록 보기')
print(hist.history.keys())
print('-'*30)

for key, value in hist.history.items():
    print('키 : ', key, ', 값 : ', value)

print(model.metrics_names)
print('-'*30)

print('model.evaluate 실행중')
score = model.evaluate(x_test, y_test, verbose=1)

print('test_acc : %.4f' % (score[1]))
print('-'*30)

print('test_loss : %.4f' % (score[0]))
print('-'*30)

import matplotlib.pyplot as plt

# 모델의 정확도에 대한 히스토리를 시각화 합니다.
plt.title('model accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')

accuracy = hist.history['accuracy']
val_accuracy = hist.history['val_accuracy']

plt.plot(accuracy)
plt.plot(val_accuracy)

plt.legend(['train', 'test'], loc='upper left')

filename = 'mnistNeuralNet01_01.png'
plt.savefig(filename)
print(filename + '저장됨')

# 모델의 손실(비용) 함수에 대한 히스토리를 시각화 합니다.
plt.figure()
plt.title('model loss')
plt.xlabel('loss')
plt.ylabel('val_loss')

loss = hist.history['loss']
val_loss = hist.history['val_loss']

plt.plot(loss)
plt.plot(val_loss)

plt.legend(['train', 'test'], loc='upper left')

filename = 'mnistNeuralNet01_02.png'
plt.savefig(filename)
print(filename + '저장됨')
