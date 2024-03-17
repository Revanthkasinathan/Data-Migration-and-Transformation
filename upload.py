import boto3
import os

def upload_files_to_s3(directory, bucket_name):
    s3 = boto3.client("s3",aws_access_key_id=access_key,aws_secret_access_key=secret_key)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Upload each file to S3
            s3.upload_file(file_path, bucket_name, file_path[len(directory)+1:])  # Use relative path for S3 key

if __name__ == "__main__":
    directory = '/content/unzip4'  # Directory containing extracted JSON files
    bucket_name = 's3testbucket8940'  # Your S3 bucket name

    upload_files_to_s3(directory, bucket_name)
    print("Files uploaded to S3 successfully.")
