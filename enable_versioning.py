import boto3
from botocore.exceptions import ClientError

def enable_versioning(bucket_name):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    try:
        # Enable versioning on the S3 bucket
        response = s3.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'Status': 'Enabled'
            }
        )
        print(f"Versioning enabled on bucket: {bucket_name}")
    except ClientError as e:
        print(f"Error enabling versioning: {e}")

if __name__ == "__main__":
    bucket_name = input("Enter the S3 bucket name: ")
    enable_versioning(bucket_name)
