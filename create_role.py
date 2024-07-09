import boto3
import json
import sys

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

# Get role names from command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_roles.py <role1> <role2> ... <roleN> <roles_file>")
        sys.exit(1)

    role_names = sys.argv[1:-1]
    roles_file = sys.argv[-1]

    create_roles_from_file(role_names, roles_file)
