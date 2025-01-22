import boto3

# instance_id = "i-092dd5ceca569741b"

ec2_client = boto3.client("ec2", region_name="us-west-2")

response = ec2_client.describe_instances()
# list_instance = response['Reservations']
# state = response['Reservations'][0]['Instances'][0]['State']['Name']
# if state == 'stopped':
#     print(f"Instance {instance_id} is stopped. Starting it now...")
#     ec2_client.start_instances(InstanceIds=[instance_id])
#     print(f"Instance {instance_id} has been started.")
# elif state == 'running':
#     print(f"Instance {instance_id} is already running.")
# else:
#     print(f"Instance {instance_id} is in '{state}' state. No action taken.")
# print(list_instance)
# print(f"Instance_id = {instance_id} , state = {state}")

# for reservation in response['Reservations']:
#     for instance in reservation['Instances']:
#         print(f"Instance_id = {instance['InstanceId']}, state = {instance['State']['Name']}")
#         value_of_instance_id = instance["InstanceId"]
#         state = instance['State']['Name']
#         print(value_of_instance_id)
#         print(state)
#         if state == "stopped":
#             ec2_client.start_instances(InstanceIds=[value_of_instance_id])
#             print(f"ths instance {instance[value_of_instance_id]} is {state}")
#         elif state == "running":
#             print(f"instance {instance['InstanceId']} is already running")


my_vpc = "myvpc"
filter = [
    { "Name": "vpc-id", "Values": [my_vpc]},
    {"Name": "instance-state-names", "Values": ['pending','running','stopping','stopped']}
]
instance_ids=[]
response=ec2_client.describe_instances(Filter=filter)
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])
# Terminate instances if any are found
if instance_ids:
    print(f"Terminating instances: {instance_ids}")
    ec2_client.terminate_instances(InstanceIds=instance_ids)
else:
    print(f"No instances found in VPC '{my_vpc}'.")