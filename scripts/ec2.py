import boto3

REGION = "ap-southeast-1"

ec2 = boto3.client("ec2", region_name=REGION)

def check_ec2():
    report = []

    response = ec2.describe_instances()

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]

            if state == "stopped":
                report.append([
                    "EC2",
                    instance_id,
                    "Stopped",
                    "Consider terminating or starting the instance"
                ])
            else:
                report.append([
                    "EC2",
                    instance_id,
                    state,
                    "No Action Required"
                ])

    return report
