# 04_makeCsv.py

import random
import pandas as pd

result = []
mycolumns = ('번호', '이름', '나이')

for idx in range(1, 11):
    sublist = []
    sublist.append(10*idx)
    sublist.append('김철수' + str(idx))
    sublist.append(random.randint(20, 40))
    result.append(sublist)
print(result)
print(type(result))

myframe = pd.DataFrame(result, columns=mycolumns)
print(myframe)
filename = 'result01.csv'

myframe.to_csv(filename, encoding='utf-8', mode='w')

print("finished")