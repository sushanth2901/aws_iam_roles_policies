import boto3
import json
import sys

def create_policy(policy_name, policy_document):
    client = boto3.client('iam')
    
    response = client.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document)
    )
    
    print(f"Policy {policy_name} created successfully.")
    print(response)

def create_policies_from_file(policy_names, policies_file):
    # Read the policies from the JSON file
    with open(policies_file, 'r') as file:
        policies_data = json.load(file)
    
    # Check if the number of policy names matches the number of policy documents
    if len(policy_names) != len(policies_data['policies']):
        raise ValueError("The number of policy names does not match the number of policy documents.")
    
    # Iterate through the list of policy documents and create each policy with the given names
    for policy_name, policy in zip(policy_names, policies_data['policies']):
        create_policy(policy_name, policy['PolicyDocument'])

# Get policy names from command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_policies.py <policy1> <policy2> ... <policyN> <policies_file>")
        sys.exit(1)

    policy_names = sys.argv[1:-1]
    policies_file = sys.argv[-1]

    create_policies_from_file(policy_names, policies_file)
