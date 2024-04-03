import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test-table')

def lambda_handler(event, context):
    # Parse request body
    data = json.loads(event['body'])

    # Extract data from request body
    item_id = data['id']
    item_data = data['data']

    # Put item into DynamoDB
    table.put_item(
        Item={
            'id': item_id,
            'data': item_data
        }
    )

    # Return response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item added to DynamoDB'})
    }
    return response
