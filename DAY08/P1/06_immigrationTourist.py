# 06_immigrationTourist.py

# 출입국 관광 통계 서비스

import urllib.parse
import urllib.request
import json
import math


def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 : # 문제 없슴
            # print('url 정보 : [%s]' % (url))
            # print('발생 시각 : [%s]' % (datetime.datetime.now()))
            return response.read().decode('utf-8')

    except Exception as err :
        # print(err)
        # print('발생 시각 : [%s]' % (datetime.datetime.now()))
        print('오류 발생 url : [%s]' % (url))
        return None

access_key = 'iqMAN42GGXnnkDlrczqgRtwuyhemqNOGWSB%2Bm0fuPTB%2F13sdh34fsjNY5MLDlu%2B7G2BGMsKH6yGKu9qY2AEMGQ%3D%3D'

def getNatVisitor(yyyymm, nat_cd, ed_cd):
    end_point = 'http://openapi.tour.go.kr/openapi/service'
    end_point += '/EdrcntTourismStatsService'
    end_point += '/getEdrcntTourismStatsList'

    parameters = '?'
    parameters += '_type=json'  # json으로 받겠다.
    parameters += '&serviceKey=' + access_key
    parameters += '&YM=' + yyyymm        # 년월
    parameters += '&NAT_CD=' + nat_cd    # 국가 코드
    parameters += '&ED_CD=' + ed_cd      # 출국/입국

    url = end_point + parameters

    retData = getRequestUrl(url)

    if retData == None:
        return None
    else:
        return json.loads(retData)

def main():
    jsonResult = []

    # 중국 : 112, 일본 : 130, 미국 : 275
    nation = '중국'
    national_code = '112'
    cd_ed = 'E' #방한한 외국인 관광객

    nStartYear = 2015
    nEndYear = 2020

    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            yyyymm = '%s%s' % (str(year), str(month).zfill(2))

            jsonData = getNatVisitor(yyyymm, national_code, cd_ed)
            # print(jsonData)

            if jsonData['response']['header']['resultMsg'] == 'OK':
                # krName = jsonData['response']['body']['items']['item']['natKorNm']
                # krName = krName.replace(' ', '')
                totalCount = jsonData['response']['body']['totalCount']
                if totalCount != 0:
                    iTotalVisit = jsonData['response']['body']['items']['item']['num']
                # print('%s_%s : %s' % (krName, yyyymm, iTotalVisit))

                jsonResult.append({'nat_name':nation, 'nat_cd':national_code, 'yyyymm':yyyymm, 'visit_cnt':iTotalVisit})
            # break # 삭제
        # end inner for
        # break # 삭제
    # end outer for

    # 파일 저장하기
    # touristResource(서울특별시 2015~2019).json
    savedFilename = 'immigrationTourist %s(%s)_(%d~%d).json'
    filename = savedFilename % (nation, national_code, nStartYear, nEndYear)

    with open(filename, 'w', encoding='utf-8') as outfile :
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print(filename + ' 파일 저장됨')

if __name__ == '__main__' :
    main()

print('-'* 30)
