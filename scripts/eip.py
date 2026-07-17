import boto3

REGION = "ap-southeast-1"

ec2 = boto3.client("ec2", region_name=REGION)

def check_eip():
    report = []

    response = ec2.describe_addresses()

    for address in response["Addresses"]:
        allocation_id = address.get("AllocationId", "N/A")

        if "AssociationId" not in address:
            report.append([
                "Elastic IP",
                allocation_id,
                "Unused",
                "Release Elastic IP"
            ])
        else:
            report.append([
                "Elastic IP",
                allocation_id,
                "In Use",
                "No Action Required"
            ])

    return report
