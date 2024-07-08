import boto3
import json
import sys

policy_name = sys.argv[1]

client = boto3.client('iam')

policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "*"
        }
    ]
}

response = client.create_policy(
    PolicyName=policy_name,
    PolicyDocument=json.dumps(policy_document)
)

print(response)
