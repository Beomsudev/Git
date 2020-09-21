# 01_sqlite.py

import sqlite3

# conn = sqlite3.connect(database='sqlite.db')
# print(type(conn))
#
# mycursor = conn.cursor()
#
# try:
#     mycursor.execute("drop table students")
# except sqlite3.OperationalError as err:
#     print("테이블이 존재하지 않습니다.")
#     print(err)
#
# mycursor.execute(
#     '''create table students
#     (id test primary key, name text, birth text)''')
#
# sql = "insert into students(id, name, birth) values('lee', '이승기', '1989/11/11')"
# mycursor.execute(sql)
#
# sql = "insert into students(id, name, birth) values('kang', '강감찬', '1111/11/11')"
# mycursor.execute(sql)
#
# datamylist = [('jo', '조용필', '1985/12/31'), ('ko', '고아라', '1970/07/17'), ('sim', '심형래', '1950/06/06')]
# sql = "insert into students(id, name, birth) values(?, ?, ?)"
# mycursor.executemany(sql, datamylist)
#
# conn.commit()
#
# findID = 'ko'
# sql = "select * from students where id = '%s'"
#
# mycursor.execute(sql % (findID))
#
# result = mycursor.fetchone()
# print(type(result))
# print(result)
# if result != None :
#     print('아이디 : '+ result[0], end='')
#     print(', 이름 : '+ result[1], end='')
#     print(', 생일 : '+ result[2], end='')
# else:
#     print('문제가 있습니다.')
# print('-'*20)
#
# sql = 'select * from students order by name desc' # asc <-> desc
#
# for id, name, birth in mycursor.execute(sql):
#     print(id + '#' + name + '#' + birth)
# print('-'*20)
#
# sql = "select * from students where name like '%이%'"
# mycursor.execute(sql)
# print(mycursor.fetchall())
#
# # 'id'가 lee인 친구의 이름을 '이문세'로 바꾸세요.
# pid = 'lee'
# newname = '이문세'
# sql = "update students set name = '%s' where id = '%s'"
# mycursor.execute(sql % (newname, pid))
#
# # 'id'가 sim인 친구의 데이터를 삭제하세요.
# pid = 'sim'
# sql = "delete from students where id = '%s'"
# mycursor.execute(sql % (pid))
#
# conn.commit()
#
# sql = 'select * from students order by name asc'
#
# for id, name, birth in mycursor.execute(sql):
#     print(id + '#' + name + '#' + birth)
# print('-'*20)
#
# mycursor.close()
# conn.close()

def getAllInfo( mycursor ):
    for onetuple in mycursor :
        print( '아이디 : ' + onetuple[0], end='')
        print( ', 과목 : ' + onetuple[1], end='')
        print( ', 점수 : ' + str(onetuple[2]), end='')
        print()

conn = sqlite3.connect('sqlitedb.db')
mycursor = conn.cursor()

try:
    mycursor.execute("drop table sungjuk")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')

mycursor.execute('''create table sungjuk
            (id text, subject text, jumsu integer)''')

mycursor.execute('insert into sungjuk values ("lee","java", 10)')
mycursor.execute('insert into sungjuk values ("lee","html", 10)')
mycursor.execute('insert into sungjuk values ("lee","python", 30)')

conn.commit()

datamylist = [ ('jo', 'java', 40), ('jo', 'html', 50), ('jo', 'python', 60), \
              ('ko', 'java', 70), ('ko', 'html', 80), ('ko', 'python', 90), ]
mycursor.executemany('insert into sungjuk values(?,?,?)', datamylist)
conn.commit()

sql = "select * from sungjuk"
mycursor.execute(sql)

print('-' * 40)
getAllInfo( mycursor ) # 함수 형태로 구현

print('-' * 40)
sql = 'select * from sungjuk order by id, subject'
for row in mycursor.execute(sql):
    print(row)
print('-' * 40)

mycursor.close()
conn.close()
print('-' * 40)
print('작업 완료^^')