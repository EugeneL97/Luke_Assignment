import boto3 
from credentials import get_aws_credentials

aws_access_key_id, aws_secret_access_key, region = get_aws_credentials()

dynamodb = boto3.resource('dynamodb', region_name = region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

table = dynamodb.Table('test-table')

print(table.creation_date_time)