import boto3

REGION = "ap-southeast-1"

rds = boto3.client("rds", region_name=REGION)

def check_rds():
    report = []

    response = rds.describe_db_instances()

    for db in response["DBInstances"]:
        db_id = db["DBInstanceIdentifier"]
        status = db["DBInstanceStatus"]

        if status == "stopped":
            report.append([
                "RDS",
                db_id,
                "Stopped",
                "Consider deleting or starting the DB"
            ])
        else:
            report.append([
                "RDS",
                db_id,
                status,
                "No Action Required"
            ])

    return report
