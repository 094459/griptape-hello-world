import boto3
from botocore.exceptions import ClientError

SAGEMAKER_IAM_ROLE_NAME = 'Sagemaker-Endpoint-Creation-Role'
SAGEMAKER_ENDPOINT_NAME = "huggingface-pytorch-sagemaker-endpoint"

sagemaker_client = boto3.client('sagemaker')
iam = boto3.client('iam')


try:
    # verify endpoint exists
    endpoint = sagemaker_client.describe_endpoint(EndpointName=SAGEMAKER_ENDPOINT_NAME)

    print(f"Endpoint {endpoint['EndpointName']} found, shutting down")

    try: # delete both endpoint and configuration
        sagemaker_client.delete_endpoint(
            EndpointName=SAGEMAKER_ENDPOINT_NAME
        )
        sagemaker_client.delete_endpoint_config(
            EndpointConfigName=SAGEMAKER_ENDPOINT_NAME
        )
        print(f"Endpoint {SAGEMAKER_ENDPOINT_NAME} shut down")
    except ClientError as e:
        print(e)
except:
    print(f"Endpoint {SAGEMAKER_ENDPOINT_NAME} does not exist in account {boto3.client('sts').get_caller_identity().get('Account')}")
    
# delete IAM role created

role_name=SAGEMAKER_IAM_ROLE_NAME
try:
    for item in iam.list_attached_role_policies(RoleName=role_name)['AttachedPolicies']:
        policy_arn = item['PolicyArn']
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
        print(f"Detached policy {policy_arn}")
    for item in iam.list_role_policies(RoleName=role_name)['PolicyNames']:
        policy_name = item
        iam.delete_role_policy(RoleName=role_name, PolicyName=policy_name)
        print(f"Deleted inline policy {policy_name}")
    iam.delete_role(RoleName=role_name)
    print(f"Deleted role {role_name}")
except ClientError as e:
        print(e)