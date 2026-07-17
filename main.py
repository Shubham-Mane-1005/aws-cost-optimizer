import csv
import os

from scripts.ec2 import check_ec2
from scripts.ebs import check_ebs
from scripts.s3 import check_s3
from scripts.rds import check_rds
from scripts.eip import check_eip
from scripts.elb import check_elb

os.makedirs("reports", exist_ok=True)

report = []

report.extend(check_ec2())
report.extend(check_ebs())
report.extend(check_s3())
report.extend(check_rds())
report.extend(check_eip())
report.extend(check_elb())

with open("reports/cost-report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Resource Type",
        "Resource ID",
        "Status",
        "Recommended Action"
    ])

    writer.writerows(report)

print("=" * 50)
print("AWS Cost Optimization Report Generated")
print("=" * 50)
print(f"Total Findings : {len(report)}")
print("Report Saved : reports/cost-report.csv")
