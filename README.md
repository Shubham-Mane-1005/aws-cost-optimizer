# AWS Cost Optimization Automation

## Project Overview

AWS Cost Optimization Automation is a Python-based project that scans AWS resources, identifies unused resources, generates a cost optimization report, and sends email notifications using Amazon SNS.

The project helps reduce unnecessary AWS costs by detecting idle cloud resources and recommending actions such as deleting or releasing unused resources.

---

# Architecture

```text
                         +----------------------+
                         |      main.py         |
                         | Python + Boto3       |
                         +----------+-----------+
                                    |
        ---------------------------------------------------------
        |           |           |          |          |          |
        ▼           ▼           ▼          ▼          ▼          ▼
     Amazon      Amazon      Amazon    Amazon    Elastic     Elastic
      EC2          EBS          S3        RDS       IP          ELB
        |           |           |          |          |          |
        ----------------------------------------------------------
                             AWS Resource Scan
                                    |
                                    ▼
                     Generate Cost Optimization Report
                                    |
                                    ▼
                        reports/cost-report.csv
                                    |
                                    ▼
                          Amazon SNS Notification
                                    |
                                    ▼
                            Email Notification
```

---

# Features

- Detect Stopped EC2 Instances
- Detect Unattached EBS Volumes
- Detect Empty S3 Buckets
- Detect RDS Snapshots
- Detect Unassociated Elastic IPs
- Detect Load Balancers
- Generate CSV Cost Report
- Send Email Notifications using Amazon SNS

---

# AWS Services Used

- Amazon EC2
- Amazon EBS
- Amazon S3
- Amazon RDS
- Elastic IP
- Elastic Load Balancer
- Amazon SNS
- IAM
- AWS CLI

---

# Technologies Used

- Python
- Boto3
- AWS CLI
- Git
- GitHub
- Ubuntu Linux

---

# Project Structure

```text
aws-cost-optimizer/
│
├── scripts/
│   ├── ec2.py
│   ├── ebs.py
│   ├── s3.py
│   ├── rds.py
│   ├── eip.py
│   └── elb.py
│
├── reports/
│   └── cost-report.csv
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Shubham-Mane-1005/aws-cost-optimizer.git
```

## Move to Project Directory

```bash
cd aws-cost-optimizer
```

## Install Dependencies

```bash
pip install boto3 pandas
```

## Configure AWS CLI

```bash
aws configure
```

Enter:

- AWS Access Key
- AWS Secret Key
- Region
- Output Format

---

# Run the Project

```bash
python3 main.py
```

---

# Sample Report

| Resource Type | Resource ID | Status | Recommendation |
|--------------|-------------|--------|----------------|
| EC2 | i-xxxxxxxx | Stopped | Terminate |
| EBS | vol-xxxxxxxx | Unattached | Delete |
| S3 | my-bucket | Empty | Review/Delete |
| RDS Snapshot | snapshot-01 | Available | Review/Delete |
| Elastic IP | 13.xxx.xxx.xxx | Unused | Release |
| Load Balancer | my-alb | Active | Review |

---

# Project Workflow

```
AWS Resources
      │
      ▼
Python (Boto3)
      │
      ▼
Resource Scanning
      │
      ▼
Cost Analysis
      │
      ▼
Generate CSV Report
      │
      ▼
Amazon SNS
      │
      ▼
Email Notification
```

---

# Future Enhancements

- HTML Report Generation
- AWS Lambda Automation
- Amazon EventBridge Scheduling
- CloudWatch Dashboard
- AWS Cost Explorer Integration
- QuickSight Dashboard

---

# GitHub Repository

Repository:

https://github.com/Shubham-Mane-1005/aws-cost-optimizer

GitHub Profile:

https://github.com/Shubham-Mane-1005

---

# Author

**Shubham Mane**

Cloud & DevOps Engineer
