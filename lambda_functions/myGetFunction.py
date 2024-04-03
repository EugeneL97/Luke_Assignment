import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test-table')

def lambda_handler(event, context):
    # Get all items from DynamoDB table
    response = table.scan()

    # Extract item data from response
    items = response['Items']

    # Return response
    response = {
        'statusCode': 200,
        'body': json.dumps(items)
    }
    return response
