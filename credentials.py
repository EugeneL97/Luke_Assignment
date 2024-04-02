import configparser

def get_aws_credentials():
    config = configparser.ConfigParser()
    config.read('credentials.ini')

    aws_access_key_id = config.get('default', 'aws_access_key_id')
    aws_secret_access_key = config.get('default', 'aws_secret_access_key')
    region = config.get('default', 'region')

    return aws_access_key_id, aws_secret_access_key, region