import boto3

REGION = "ap-southeast-1"

elb = boto3.client("elbv2", region_name=REGION)

def check_elb():
    report = []

    try:
        response = elb.describe_load_balancers()

        for lb in response["LoadBalancers"]:
            report.append([
                "ELB",
                lb["LoadBalancerName"],
                lb["State"]["Code"],
                "Review if still required"
            ])

    except Exception:
        pass

    return report
