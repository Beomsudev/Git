# 03_sqliteEx03.py

import sqlite3

class SqliteDB:
    def __init__(self, dbname):
        print('생성자 출력')
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def __del__(self): # 소멸자(마감처리 용도)
        print('소멸자 출력')
        self.cursor.close()
        self.conn.close()
    def getJoinData(self):  # 조인 데이터
        sql = " select st.id, st.name, st.birth, sg.subject, sg.jumsu"

        sql += " from students st join sungjuk sg"

        sql += " on st.id = sg.id;"

        result = self.cursor.execute(sql)
        return result

    def getSubQuery(self, name):
        pass
        sql = " select * from sungjuk"
        sql += " where id = (select id from students where name = '%s')"

        result = self.cursor.execute(sql % (name))

        return result

    def getJumsu(self, name):
        pass


dbname = 'sqlitedb.db'
mydb = SqliteDB(dbname)

dataset = mydb.getJoinData()
for row in dataset:
    print(row)

print('#' * 30)

who = '이문세'
dataset = mydb.getSubQuery(who)
for (id, subject, jumsu) in dataset:
    print('아이디 : ', id, end='', sep='')
    print(', 과목 : ', subject, end='', sep='')
    print(', 점수 : ', jumsu, end='', sep='')
    print()


print('#' * 30)





print('finished')
