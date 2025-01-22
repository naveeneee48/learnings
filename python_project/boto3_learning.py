import boto3

ec2_client=boto3.client("ec2")
response=ec2_client.describe_instances()
print(response)


# Print instance details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")


# Replace with your EC2 instance ID
instance_id = 'i-0b12faf13bfce23bf'

# Create an EC2 client
# ec2_client = boto3.client('ec2')

# Start the instance
response = ec2_client.start_instances(InstanceIds=[instance_id])
print(f"Starting EC2 instance: {instance_id}")



