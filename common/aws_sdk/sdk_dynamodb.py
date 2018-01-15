from __future__ import print_function # Python 2/3 compatibility
from common.constants.billing_info import BillingInfo
from common.constants.dynamodb.constant_dynamodb import ConstDynamodb
import boto3


# dynamodb 클라이언트
client      = boto3.client('dynamodb', region_name=BillingInfo.SEOUL)

# dynamodb를 생성한다
def createTable() :
    table   = client.create_table(
        TableName= ConstDynamodb.TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': ConstDynamodb.PRIMARY_KEY,
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': ConstDynamodb.SORT_KEY,
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': ConstDynamodb.PRIMARY_KEY,
                'AttributeType': 'S'
            },
            {
                'AttributeName': ConstDynamodb.SORT_KEY,
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

# dynamobb table을 삭제한다
def deleteTable() :
    client.delete_table (TableName = ConstDynamodb.TABLE_NAME)

# dynamodb table 목록을 불러온다
def listTables() :
    return client.list_tables()

# table 정보를 불러온다
def describeTable(tableNm) :
    return client.describe_table(TableName=tableNm)

# dyanamodb table에 데이터 insert한다
def putItem(sortKey, product, dict) :
   
    # 로컬 
    # dynamodb = boto3.resource('dynamodb', region_name=Info.SEOUL, endpoint_url="http://localhost:8000")
    # 콘솔
    dynamodb    = boto3.resource('dynamodb', region_name=BillingInfo.SEOUL)
    table       = dynamodb.Table(ConstDynamodb.TABLE_NAME)

    dict[ConstDynamodb.OFFER_CODE]  = product
    dict[ConstDynamodb.SORT_KEY]    = sortKey
    dict[ConstDynamodb.PRIMARY_KEY] = dict[ConstDynamodb.PRIMARY_KEY]

    table.put_item(Item = dict)
