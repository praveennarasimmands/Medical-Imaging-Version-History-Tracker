import boto3
from botocore.exceptions import ClientError

def list_image_versions(bucket_name, file_name):
    s3 = boto3.client('s3')
    
    try:
        # List versions of the image in the specified S3 bucket
        response = s3.list_object_versions(Bucket=bucket_name, Prefix=file_name)
        
        versions = response.get('Versions', [])
       
