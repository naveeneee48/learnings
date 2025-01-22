import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List VPCs
response = ec2.describe_vpcs()

for vpc in response['Vpcs']:
    print(f"VPC ID: {vpc['VpcId']}, CIDR: {vpc['CidrBlock']}")
import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List VPCs
response = ec2.describe_vpcs()

for vpc in response['Vpcs']:
    print(f"VPC ID: {vpc['VpcId']}, CIDR: {vpc['CidrBlock']}")
