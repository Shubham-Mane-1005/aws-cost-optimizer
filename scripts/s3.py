import boto3

s3 = boto3.client("s3")

def check_s3():
    report = []

    buckets = s3.list_buckets()

    for bucket in buckets["Buckets"]:
        bucket_name = bucket["Name"]

        objects = s3.list_objects_v2(Bucket=bucket_name)

        if objects.get("KeyCount", 0) == 0:
            report.append([
                "S3",
                bucket_name,
                "Empty",
                "Review/Delete"
            ])
        else:
            report.append([
                "S3",
                bucket_name,
                "In Use",
                "No Action Required"
            ])

    return report
