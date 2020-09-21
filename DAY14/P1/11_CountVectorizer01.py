# 11_CountVectorizer01.py

from sklearn.feature_extraction.text import CountVectorizer

# CountVectorizer : 문자열에서 단어 토큰을 생성하여 BOW로 인코딩된 벡터를 생성해줍니다.
# df : document-frequency
# min_df = 2 : 최소 빈도가 2번 이상인 단어들만 ..
# stop_words = 불용어 (제외)

vectorizer = CountVectorizer(min_df=2, stop_words=['친구'])
print(type(vectorizer))

sentences = ['우리 아버지 여자 친구 이름은 홍길동 홍길동', '홍길동 여자 친구 이름은 심순애 심순애', '여자 친구 있나요.']

mat = vectorizer.fit(sentences)
print(type(mat))

print(mat.vocabulary_)

# 토큰
features = vectorizer.get_feature_names()
print(type(features))
print(features)

print('불용어')
print(vectorizer.get_feature_names())

myword = [sentences[0]]
print('myword : ', myword)

myarray = vectorizer.transform(myword).toarray()
print(type(myarray))

'''
0('여자')이 1번 1('이름은')이 1번, 2('홍길동')가 1번 나왔습니다.
myarray :  [[1 1 3]]
단어 사전 : {'여자': 0, '이름은': 1, '홍길동': 2}
myword :  ['우리 아버지 여자 친구 이름은 홍길동 홍길동 홍길동']

'''


print('myarray : ', myarray)

print('finished')
