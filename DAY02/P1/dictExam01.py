# dictExam01.py
# dict(사전) : 키와 값으로 구성되어 있는 데이터 구조
# 순서를 따지지 않는 자료 구조
# 중괄호를 사용
# 키와 값은 콜론으로 구분하고, 항목들은 콤마로 구분한다.
# 예시 : {키1:값1, 키2:값2, 키3:값3 ...}
# 관련 함수 : dict()
# 함수 : get(키, 기본값), clear(), del()

mydict = {"name":"홍길동", "phone":"01011112222", "birth":"12/25"}

# 사전 이름에 "키"를 넣어 주면 "값"을 구할 수 있습니다.
print(mydict["birth"])

# 쓰기 :
mydict["phone"] = "01033335555"

# 존재하지 않는 키는 insert가 된다.
mydict["adress"] = "마포구 공덕동"

# 존재하지 않는 키는 KeyError 오류가 발생합니다.
# print(mydict["age"])

# get("찾을키", 기본값)
print(mydict.get("name", 10))

print(mydict)

# 해당 키를 제거합니다
del mydict["phone"]

print(mydict)

if "adress" in mydict : # in 함수 안에 들어 있으면 true 아니면 false
    print("주소 있음")
else :
    print("주소 없음")

mydict.clear()

print(mydict)

mydict = {} # 비어있는 사전
mydict["hong"] = ["홍길동", 23] # 값에는 모든 데이터 타입 삽입 가능 ex) list, tuple
mydict["park"] = ["박영희", 35]
print(mydict)