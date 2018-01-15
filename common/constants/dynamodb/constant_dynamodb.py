# dynamodb와 관련된 constant

class ConstDynamodb(object) :

    # 테이블 관련
    TABLE_NAME  = "PricingData"     # 테이블 이름
    PRIMARY_KEY = "RateCode"        # 생성되는 table에서 primary key를 지정
    SORT_KEY    = "Version"         # index key
    OFFER_CODE  = "OfferCode"       # product name
    DATA        = "Data"            # put item할 때 기준이 되는 Attribute 값

    # Attribute 관련
    CSV_KEY     = "SKU"             # csv파일에서 key르 시작되는 행을 뽑아낼 때 구분하는 변수
    NULL        = "null"            # Attribute value가 null일 경우 들어가는 값
