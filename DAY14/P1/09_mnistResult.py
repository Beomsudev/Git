# mnistResult.py

test_acc = [0.9240, 0.9215, 0.9777, 0.9770, 0.9774]
test_loss = [0.2809, 0.2775, 0.0822, 0.1049, 0.0844]
comments = ['테스트01', '테스트02', '테스트03', '테스트04', '테스트05']

mycolor = ['b', 'g', 'r', 'c', 'y']

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

#########################################################

plt.title('테스트 케이스별 정확동')
plt.xlabel('테스트 케이스')
plt.ylabel('정확도')
plt.bar(comments, test_acc, color=mycolor)


filename = 'mnist_accuracy_graph.png'
plt.savefig(filename)
print(filename + '저장됨')

#########################################################

plt.title('테스트 케이스별 손실')
plt.xlabel('테스트 케이스')
plt.ylabel('손실')
plt.bar(comments, test_acc, color=mycolor)


filename = 'mnist_loss_graph.png'
plt.savefig(filename)
print(filename + '저장됨')