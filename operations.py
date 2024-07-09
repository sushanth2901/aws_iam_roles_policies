import sys
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


def create_role(role_name, assume_role_policy_document):
    client = boto3.client('iam')
    
    response = client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy_document)
    )
    
    print(f"Role {role_name} created successfully.")
    print(response)

def create_roles_from_file(role_names, roles_file):
    # Read the roles from the JSON file
    with open(roles_file, 'r') as file:
        roles_data = json.load(file)
    
    # Create a dictionary to map role names to their assume role policy documents
    role_map = {role['RoleName']: role['AssumeRolePolicyDocument'] for role in roles_data['roles']}
    
    # Iterate through the list of role names and create each role with the corresponding document
    for role_name in role_names:
        if role_name in role_map:
            create_role(role_name, role_map[role_name])
        else:
            print(f"Role name {role_name} not found in the roles file.")

def delete_policy(policy_arn):
    client = boto3.client('iam')
    response = client.delete_policy(
        PolicyArn=policy_arn
    )
    print(f"Policy {policy_arn} deleted successfully.")
    print(response)

def delete_role(role_name):
    client = boto3.client('iam')
    response = client.delete_role(
        RoleName=role_name
    )
    print(f"Role {role_name} deleted successfully.")
    print(response)

def attach_policy_to_role(role_name, policy_arns):
    client = boto3.client('iam')
    for policy_arn in policy_arns:
        response = client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"Policy {policy_arn} attached to role {role_name}.")
        print(response)

def detach_policy_from_role(role_name, policy_arn):
    client = boto3.client('iam')
    response = client.detach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Policy {policy_arn} detached from role {role_name}.")
    print(response)

if __name__ == "__main__":
    operation = sys.argv[1]
    if operation == "create_policy":
        policy_names = sys.argv[1:-1]
        policies_file = sys.argv[-1]
        create_policies_file(policy_names, policies_file)
        
    elif operation == "create_role":
        role_names = sys.argv[1:-1]
        roles_file = sys.argv[-1]
        create_roles_from_file(role_names, roles_file)

    elif operation == "delete_policy":
        policy_arn = sys.argv[2]
        delete_policy(policy_arn)

    elif operation == "delete_role":
        role_name = sys.argv[2]
        delete_role(role_name)

    elif operation == "attach_policy_to_role":
        role_name = sys.argv[2]
        policy_arns = sys.argv[3]
        attach_policy_to_role(role_name, policy_arns)

    elif operation == "detach_policy_from_role":
        role_name = sys.argv[2]
        policy_arn = sys.argv[3]
        detach_policy_from_role(role_name, policy_arn)
    else:
        print("Invalid operation specified.")
        sys.exit(1)
