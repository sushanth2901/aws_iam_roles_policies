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
    
    # Create a dictionary to map policy names to their documents
    policy_map = {policy['PolicyName']: policy['PolicyDocument'] for policy in policies_data['policies']}
    
    # Iterate through the list of policy names and create each policy with the corresponding document
    for policy_name in policy_names:
        if policy_name in policy_map:
            create_policy(policy_name, policy_map[policy_name])
        else:
            print(f"Policy name {policy_name} not found in the policies file.")

# Get policy names from command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_policies.py <policy1> <policy2> ... <policyN> <policies_file>")
        sys.exit(1)

    policy_names = sys.argv[1:-1]
    policies_file = sys.argv[-1]

    create_policies_from_file(policy_names, policies_file)
