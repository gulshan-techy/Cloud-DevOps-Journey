# FILTER RUNNING/STOP/STOPPING/TERMINATED EC2s 


# This Code Filter "RUNNING" EC2s Instances and Print Instance ID , State , Type
import boto3
ec2=boto3.client("ec2", region_name="eu-north-1")
response=ec2.describe_instances(
    Filters=[{"Name":"instance-state-name","Values":["running"]}])

for res in response["Reservations"]:
    for ins in res["Instances"]:
        print(f"ID: {ins['InstanceId']} | State: {ins['State']['Name']} | {ins['InstanceType']}") 

# This Code Filter "STOPPED" EC2s Instances Instances and Print Instance ID , State , Type
import boto3
ec2=boto3.client("ec2", region_name="eu-north-1")
response=ec2.describe_instances(
    Filters=[{"Name":"instance-state-name","Values":["stopped"]}])

for res in response["Reservations"]:
    for ins in res["Instances"]:
        print(f"ID: {ins['InstanceId']} | State: {ins['State']['Name']} | {ins['InstanceType']}")

# ---------------------------------------------------------
# 💡 PRO TIP: You can filter instances by changing the "Values".
# Available States: 'pending', 'running', 'shutting-down', 
#                   'terminated', 'stopping', 'stopped'
# ---------------------------------------------------------
