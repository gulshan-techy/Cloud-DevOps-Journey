import boto3 
# To Create AWS EC2 Client 
ec2 = boto3.client("ec2", region_name="eu-north-1") 

# To Fetch Instances details
response = ec2.describe_instances()

for res in response["Reservations"]:
    for ins in res["Instances"]:        
        print(f"ID         : {ins['InstanceId']}")
        print(f"STATE      : {ins['State']['Name']}")
        print(f"TYPE       : {ins['InstanceType']}")
        print(f"PUBLIC IP  : {ins.get('PublicIpAddress')}") 
        print(f"PRIVATE IP : {ins.get('PrivateIpAddress')}") 
        print("-" * 50)


# A Python automation script using the Boto3 library to fetch and display real-time details of AWS EC2 instances (ID, State, Type, IPs) without logging into the AWS Console.
