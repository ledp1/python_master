import boto3

# Use environment variables or configuration files to securely manage credentials. The example below performs the optional step of explicitly defining a session. 
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-1'
)