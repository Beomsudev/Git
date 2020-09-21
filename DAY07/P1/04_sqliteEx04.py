# 04_sqliteEx04.py

# 텍스트의 파일을 읽어서 sqlite DB에 추가하기
filename = 'mem.txt'
myfile = open(file=filename, mode='r', encoding='utf-8')
mylist = [item.strip() for item in myfile.readlines()]
print(mylist)
mylist.clear()

import sqlite3

conn = sqlite3.connect('sqlitedb.db')
mycursor = conn.cursor()
# db브라우저에서는 안읽힌다. 확인/ 
sql = 'insert into members(id, name) values(?, ?)'
for item in mylist:
    columnlist = item.split(',')
    mycursor.execute(sql, columnlist)   #executemany로도 할 수 있는지 응용 해보기

conn.commit()





mycursor.close()
conn.close()