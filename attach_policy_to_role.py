import boto3
import sys

role_name = sys.argv[1]
policy_arn = sys.argv[2]

client = boto3.client('iam')

response = client.attach_role_policy(
    RoleName=role_name,
    PolicyArn=policy_arn
)

print(response)
