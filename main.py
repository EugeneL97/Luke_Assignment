import boto3 

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName = 'users',
    KeySchema = [
        {
            'AttributeName' : 'username',
            'KeyType' : 'HASH'
        },
        {
            'AttributeName' : 'last_name',
            'KeyType' : 'RANGE'
        }
    ],
)
