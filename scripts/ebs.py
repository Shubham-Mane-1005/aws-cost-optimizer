import boto3

REGION = "ap-southeast-1"

ec2 = boto3.client("ec2", region_name=REGION)

def check_ebs():
    report = []

    volumes = ec2.describe_volumes()

    for volume in volumes["Volumes"]:
        volume_id = volume["VolumeId"]

        if len(volume["Attachments"]) == 0:
            report.append([
                "EBS",
                volume_id,
                "Unattached",
                "Delete unused volume"
            ])
        else:
            report.append([
                "EBS",
                volume_id,
                "In Use",
                "No Action Required"
            ])

    return report
