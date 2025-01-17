import boto3
import os
from botocore.exceptions import ClientError
from datetime import datetime

def upload_image_to_s3(bucket_name, file_path, patient_id):
    s3 = boto3.client('s3')

    # Extract image file name from the path
    file_name = os.path.basename(file_path)
    
    # Metadata to associate with the image
    metadata = {
        'PatientID': patient_id,
        'ScanDate': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    try:
        # Upload the image to S3
        response = s3.upload_file(
            file_path,
            bucket_name,
            file_name,
            ExtraArgs={'Metadata': metadata}
        )
        print(f"Image {file_name} uploaded successfully to bucket: {bucket_name}")
    except ClientError as e:
        print(f"Error uploading image: {e}")

if __name__ == "__main__":
    bucket_name = input("Enter the S3 bucket name: ")
    file_path = input("Enter the path to the medical image: ")
    patient_id = input("Enter the patient ID: ")
    
    upload_image_to_s3(bucket_name, file_path, patient_id)
