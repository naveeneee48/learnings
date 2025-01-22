
import boto3

ec2_client=boto3.client("ec2")
response=ec2_client.describe_addresses()
for address in response['Addresses']:
    if 'InstanceId' not in address:
       print(f"elastic IP {address} is not used")
       ec2_client.release_addresses(AllocationId=address['AllocationId'])