# 02_correlationAnalysis.py

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='Malgun Gothic')

corr_list = [] # 상관 관계 분석 결과 저장
mychart = './mychart/'  # 그래프 생성 폴더

def correlation(x, y):  # 상관 계수 구하는 함수
    bar_x = x.mean()
    bar_y = y.mean()

    bunja = np.sum((x - bar_x)*(y - bar_y))
    # print('분자 : ', bunja)

    left = np.sum((x - bar_x)**2)
    right = np.sum((y - bar_y)**2)
    bunmo = np.sqrt(left * right)
    # print('분모 : ', bunmo)

    return bunja / bunmo

def setScatterGraph(tour_table, visit_table, tourpoint):
    # tour_table : 관광지 입장 정보
    # fv_table : 3개국 관광객 수
    # tourpoint : 관광지 이름(예시 : 경복궁)
    tour = tour_table[tour_table['resNm'] == tourpoint]
    merge_table = pd.merge(tour, visit_table, left_index=True, right_index=True)
    # print('#' * 30)
    # print(merge_table)
    mylist = [['china', '중국인'],['usa', '미국인'],['japan', '일본인']]
    imsi = []
    imsi.append(tourpoint) # 방문지를 추가

    fig = plt.figure()  # 그래프 그릴 때 새로운 도화지를 준비한다.

    print('[' + tourpoint + '] 작업중 입니다.')
    for onedata in mylist:
        plt.xlabel(onedata[1] + '입국수') # ex) 중국인 입국수
        plt.ylabel('외국인 입장객수')

        # 해당 국가의 컬럼만 추출
        x_data = list(merge_table[onedata[0]])
        y_data = list(merge_table['ForNum'])

        cor = correlation(np.array(x_data), np.array(y_data))
        cor = round(cor, 6)

        if cor == 0:
            print('상관 계수가 0입니다')
            return

        plt.title(tourpoint + '-' + onedata[1] + '상관 관계 분석(' + str(cor) + ')')
        plt.scatter(x_data, y_data, edgecolors='none', alpha=0.75, s=6, c='black')
        plt.savefig(mychart + tourpoint + '(' + onedata[1] + ').png')     # 해당 이미지를 파일 형식으로 저장하는 함수

        mytuple = (onedata[1], cor) #('중국인', 상관계수)
        imsi.append(mytuple) # ex) ['창덕궁', ('중국인', 상관계수)]

    corr_list.append(imsi)

# end def setScatterGraph

def main():
    if not os.path.exists(mychart):
        os.mkdir(mychart)

    filename = './data/touristResourceStat(서울특별시 2015~2019).json'   # 경로의 맨앞의 .은 현재 폴더, ..은 상위 폴더
    jsonTp = json.loads(open(filename, 'rt', encoding='utf-8').read())

    tour_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'resNm', 'ForNum'))

    print('-' * 30)

    # 'yyyymm' 컬럼을 색인으로 지정하세요. (set_index)
    tour_table = tour_table.set_index('yyyymm')
    print(tour_table.head())

    print('#' * 30)

    ########################################################################################################
    # 미국
    filename = './data/immigrationTouristStat 미국(275)_(2015~2019).json'   # 경로의 맨앞의 .은 현재 폴더, ..은 상위 폴더
    jsonTp = json.loads(open(filename, 'rt', encoding='utf-8').read())

    usa_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'visit_cnt'))

    print('-' * 30)

    # 'visit_cht' 컬럼을 국가 이름으로 변경 (rename)
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    # 'yyyymm' 컬럼을 색인으로 지정하세요. (set_index)
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table.head())

    print('#' * 30)

    ########################################################################################################
    # 일본
    filename = './data/immigrationTouristStat 일본(130)_(2015~2019).json'  # 경로의 맨앞의 .은 현재 폴더, ..은 상위 폴더
    jsonTp = json.loads(open(filename, 'rt', encoding='utf-8').read())

    japan_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'visit_cnt'))

    print('-' * 30)

    # 'visit_cht' 컬럼을 국가 이름으로 변경 (rename)
    japan_table = japan_table.rename(columns={'visit_cnt': 'japan'})
    # 'yyyymm' 컬럼을 색인으로 지정하세요. (set_index)
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table.head())

    print('#' * 30)

    ########################################################################################################
    # 중국
    filename = './data/immigrationTouristStat 중국(112)_(2015~2019).json'  # 경로의 맨앞의 .은 현재 폴더, ..은 상위 폴더
    jsonTp = json.loads(open(filename, 'rt', encoding='utf-8').read())

    china_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'visit_cnt'))

    print('-' * 30)

    # 'visit_cht' 컬럼을 국가 이름으로 변경 (rename)
    china_table = china_table.rename(columns={'visit_cnt': 'china'})
    # 'yyyymm' 컬럼을 색인으로 지정하세요. (set_index)
    china_table = china_table.set_index('yyyymm')
    print(china_table.head())

    print('#' * 30)

    ########################################################################################################

    # merge : 2개의 데이터 프레임을 합쳐 주는 기능
    fv_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    fv_table = pd.merge(fv_table, usa_table, left_index=True, right_index=True)
    print(fv_table.head())

    # resNm : 방문지(목록)
    resNm = tour_table.resNm.unique()
    print(resNm)
    for tourpoint in resNm:
        setScatterGraph(tour_table, fv_table, tourpoint)
        # break

    print('-' * 30)
    print(corr_list)

if __name__ == '__main__':
     main()
