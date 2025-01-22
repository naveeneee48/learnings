import boto3

# Initialize the IAM client
iam = boto3.client('iam')

# List all IAM users
response = iam.list_users()

for user in response['Users']:
    print(f"Username: {user['UserName']}, ARN: {user['Arn']}")
