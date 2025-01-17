import boto3
import os
from botocore.exceptions import ClientError

def get_specific_version(bucket_name, file_name, version_id, download_path):
    s3 = boto3.client('s3')
    
    try:
        # Download the specific version of the file
        response = s3.get_object(
            Bucket=bucket_name,
            Key=file_name,
            VersionId=version_id
        )

        with open(download_path, 'wb') as file:
            file.write(response['Body'].read())
        print(f"Downloaded version {version_id} of {file_name} to {download_path}")
    except ClientError as e:
        print(f"Error retrieving specific version: {e}")

if __name__ == "__main__":
    bucket_name = input("Enter the S3 bucket name: ")
    file_name = input("Enter the file name of the image: ")
    version_id = input("Enter the VersionId to retrieve: ")
    download_path = input("Enter the local path to save the image: ")
    
    get_specific_version(bucket_name, file_name, version_id, download_path)
