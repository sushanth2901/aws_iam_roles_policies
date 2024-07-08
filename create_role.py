import boto3
import json

def create_policy(policy_name, policy_document):
    client = boto3.client('iam')
    
    response = client.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document)
    )
    
    print(f"Policy {policy_name} created successfully.")
    print(response)

def create_policies_from_file(policies_file):
    with open(policies_json.json, 'r') as file:
        policies_data = json.load(file)
    
    # Iterate through the list of policies and create each one
    for policy in policies_data['policies']:
        create_policy(policy['PolicyName'], policy['PolicyDocument'])

# Example usage
create_policies_from_file('policies.json')
