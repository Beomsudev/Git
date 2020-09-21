# 02_jsonTest01.py

import json

data = {}/

# dumps() : 데이터를 읽어서 str 향테러 바꿔줌
json_str = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)
#                           한글을 그대로둠        들여쓰기    정렬
print(json_str)

# print(type(json_str))
# print('-' * 30)
#
# json_data = json.loads(json_str)
# print(json_data)
# print(type(json_data))
#
# print(json_data['name'])
# print(json_data['age'])
# print(json_data['broadcast']['sbs'])
# print('-' * 30)
