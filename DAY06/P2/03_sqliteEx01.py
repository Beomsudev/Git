# 03_sqliteEx01.py

# sqlite : 소형 개인용 데이터 저장을 위한 데이터 베이스

import sqlite3 # sqlite를 위한 모듈

# conn : 데이터 베이스에 접근하기 위한 객체
# database : 데이터 베이스 파일 이름
conn = sqlite3.connect(database='sqlitedb.db')
print(type(conn))

# cursor(커서) : 데이터 베이스 작업을 수행하고 있는 메모리 공간
mycursor = conn.cursor()

try:
    mycursor.execute("drop table students")
except sqlite3.OperationalError as err:
    print("테이블이 존재하지 않습니다.")

mycursor.execute(
    '''create table students
    (id text, name text, birth text)''')

sql = "insert into students(id, name, birth) values('lee', '이승기', '1212/12/12')"
mycursor.execute(sql)

sql = "insert into students(id, name, birth) values('kang', '강감찬', '1211/11/11')"
mycursor.execute(sql)

datamylist = [('jo', '조용필', '1234/56/78',), ('kim', '김범수', '1234/22/22',), ('감', '감우성', '1223/23/23',)]

# '?' = place holder 치환되어야 할 어떤한 값  %d로 생각하면 될듯 sqlit에 국한 된것이 아닌 데이터 베이스 전체에 해당됨
# 데이터 유형에 상관없이 외따옴표 적으면 안됨!
sql = "insert into students(id, name, birth) values(?, ?, ?)"
# mycursor.executemany(sql=sql, seq_of_parameters=datamylist)
mycursor.executemany(sql, datamylist)

conn.commit()

findId = 'kim'
sql = "select * from students where id = '%s'"

mycursor.execute(sql % (findId))

result = mycursor.fetchone()
print(result)
if result != None: # 문제있으면 출력 안하기 위함
    print('아이디 : ' + result[0], end='')
    print(', 이름 : ' + result[1], end='')
    print(', 생일 : ' + result[2], end='')
else:
    print('문제가 있습니다.')

sql = 'select * from students order by name desc'

for row in mycursor.execute(sql):
    print(row)
print('-' * 20)

for id, name, birth in mycursor.execute(sql):
    print(id + '@' + name + '@' + birth)
print('-' * 20)

sql = "select * from students where name like '%이%'"
mycursor.execute(sql)
print(mycursor.fetchall())

# 문제 있는 부분 !!!!!
# # 'id'가 lee인 친구의 이름을 '이문세로 바꾸세요.
# pid = 'lee'
# newname = '이문세'
# sql =  "update students set name = '%s' where id = '%s'"
# mycursor.execute(sql % ('newname', 'pid'))
# conn.commit()
#
# # 'id'가 kim인 친구의 데이터를 삭제하세요.
# pid = 'kim'
# sql =  "delete from students where id = '%s'"
# mycursor.execute(sql % (pid))


mycursor.close()
conn.close()        #먼저 생성된 conn이 나중에 닫힘 html과 비슷 하다!

print('finished')