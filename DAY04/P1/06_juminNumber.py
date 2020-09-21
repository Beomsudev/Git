# 06_juminNumber.py

# 다 지우고 스스로 한번 풀어보기 !

# 주민 번호는 반드시 14자리이어야 한다.
# 6번째 항목은 반드시 '-' 이어야 한다.
# 2번째 항목은 '0' or '1' 이어야 한다
# 7번째 항목은 '0', '1', '2', '3' 이어야 한다.
# isdigit를 활용 하여 - 앞뒤로 숫자인지 아닌지 체크.

def findSsn(juminno):
    if len(juminno) != 14 :
        return False
    elif juminno[6] != "-" :
        return  False
    elif not juminno[2] in ["0", "1"] :
        return False
    elif not juminno[7] in ["0", "1", "2", "3"] :
        return False
    elif not(juminno[0:6].isdigit()) or not(juminno[7:].isdigit()) :
        return False

    return True


#             0123456789abcd
juminList = ["970819-1800617", "7012261710566", "703226-1710566", "701226-5710566"]

for juminno in juminList :
    result = findSsn(juminno)
    if result == True :
       print("{}는 올바른 주민 번호".format(juminno))
    else :
       print("{}는 잘못된 주민 번호".format(juminno))

print("-" * 30)