import time
import urllib.request
import csv
import io
from common.aws_sdk.sdk_dynamodb import putItem, describeTable, createTable
from common.constants.dynamodb.constant_dynamodb import ConstDynamodb

class Pricing:

    # AWS Price List 호출하는 URL 만드는 함수
    def makePriceListUrl(projectNm) :

        # URL Header, Tail
        HEADER  = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/"
        TAIL    = "/current/index.csv"

        return HEADER + projectNm + TAIL


    # CSV 파일을 다운받고 TEXT로 변환한다
    def downloadNTansferCSV(url) :

        webpage = urllib.request.urlopen(url)
        return csv.reader(io.TextIOWrapper(webpage))

    # key와 value를 dictionary로 만든다
    def makeValDictionary(key, val) :
        # empty dictionary
        dict = {}
        for i, data in enumerate(key) :
            dict[data] = val[i] == '' and ConstDynamodb.NULL or val[i]  # value값이 ''일 경우 대체값을 넣는다

        #등록한 시간
        now = time.localtime()
        dict["regDt"] = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        return dict




class HandlingPricig:

    # handling 하는 main함수
    def handlingData(projectNm):

        start_time = time.time()
        print("--- start ---")
        # 호출()될 URL 목록
        url = Pricing.makePriceListUrl(projectNm)
        # URL을 통해 다운로드 한 CSV 파일을 TEXT로 변환한다
        print(url)
        txt = Pricing.downloadNTansferCSV(url)
        keys = None
        # csv파일을 한줄씩 읽으면서 필요한 key 또는 value값 뽑아내기
        for row in txt:
            # key가 있는 경우 key-value값을 만들어낸다
            # key-value를 만든 후 dynamodb에 insert한다
            if keys is not None:
                item = Pricing.makeValDictionary(keys, row)
                putItem(sortKey, product, item)
            # product를 찾는다
            if any((ConstDynamodb.OFFER_CODE == s) for s in row):
                product = row[1]
            # sortkey를 찾는다
            if any((ConstDynamodb.SORT_KEY == s) for s in row):
                sortKey = row[1]
            # dynamodb item의 key를 찾는다
            if any((ConstDynamodb.CSV_KEY == s) for s in row):
                keys = row

        print("--- end : %s seconds ---" % (time.time() - start_time))
