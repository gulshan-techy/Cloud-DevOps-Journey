import boto3
import time

ec2=boto3.client("ec2", region_name="eu-north-1")

response = ec2.describe_instances()
for res in response["Reservations"]:
    for ins in res["Instances"]:       
        ins_id = ins["InstanceId"]
        print(f"Instance Id and Status before Stop :- {ins['InstanceId']} | State: {ins['State']['Name']}")

# STOP/TERMINATE  EC2 Instance
ec2.stop_instances(      # use "terminate_instances" instead of "stop_instances" to delete the instance
    InstanceIds=[ins_id]
    )

print("waiting 10 seconds for initialization so that instance status can be update")
time.sleep(10)

new_response = ec2.describe_instances()
for new_res in new_response["Reservations"]:
    for new_ins in new_res["Instances"]:       
        new_ins_id = new_ins["InstanceId"]
        print(f"Instance Id and Status After Stop :- {new_ins['InstanceId']} | State: {new_ins['State']['Name']}")

# # Automation Script to Stop or Terminate AWS EC2 Instances and Verify Status Updates.
