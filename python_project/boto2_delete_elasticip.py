import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List Elastic IPs
response = ec2.describe_addresses()

# Find and release unused Elastic IPs
for address in response['Addresses']:
    if 'InstanceId' not in address:  # Check if not associated
        print(f"Releasing unused Elastic IP: {address['PublicIp']}")
        ec2.release_address(AllocationId=address['AllocationId'])
