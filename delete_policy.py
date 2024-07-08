import boto3
import sys

policy_arn = sys.argv[1]

client = boto3.client('iam')

response = client.delete_policy(
    PolicyArn=policy_arn
)

print(response)
