# 07_function05.py

# 함수의 마지막에는 return 구문이 들어갑니다.
# 만약 명시하지 않으면 return None라는 구문이 자동으로 들어감

# None : 리턴하지 않는, 의미가 없는
# void, vacant, empty, no response

def namePrint(name, age):
    print("{}님의 나이는 {}살입니다.".format(name, age))
    return None

name = "제시카"
age = 20
result = namePrint(name, age)
print(result)

if result == None:
    print("데이터를 구하지 못했습니다.")

else:
    print("참 잘했어요")

print("-" * 30)

def gugudan(su):
    rng = range(1, 10)
    for i in rng:
        print("{} * {} = {}".format(su, i, (su*i)))
    print("-" * 30)

dan = 3
gugudan(dan)


# 2, 4, 7단을 출력 해보세요.

list_dan = [2, 4, 7]
for aaa in list_dan:
    gugudan(aaa)

# 2단이면 [2, 4, 6, ..., 18] 형식으로 출력되는 함수를 만드시오.
# 못품 스스로 다시 풀어보기 !!

def gugu_list(n):
    result = [n*idx for idx in range(1, 10)]
    print(result)

dan = 5
print(gugu_list(dan))
print("-" * 30)

# 2단부터 4단까지 각 단의 결과를 list 형식으로 출력하시오
# 혼자 못품 다시 풀어보기!!!!

# dan = [2, 3, 4]
# mylist = []
# for aaa in dan:
#     gugu_list(aaa)
#     mylist.append(aaa)
#
# print(mylist)
def Gugu2(n, m):
    for x in range(n, m+1):
        result = [x*idx for idx in range(1, 10)]
        # print(result)
        # print("-" * 30)

    return result

n, m = 2, 4
print(Gugu2(n, m))



print("finished")
