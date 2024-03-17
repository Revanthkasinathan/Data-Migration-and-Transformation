# Data-Migration-AND-Transformation

**Problem Statement:**

The objective is to utilize the request method to download the zip file from the provided URL, extract its contents, and subsequently upload the data to AWS S3. Following this, a Lambda function will be employed to trigger the data to be stored in the database.

**Technology Stack Used**

•	Python

•	AWS S3

•	AWS Lambda

•	AWS DynamoDB

•	AWS IAM

**REQUIRED LIBRARIES:**
1.	requests
2.	zipfile
3.	boto3
4.	Json

**Approach**


To begin, utilize the request library to download the JSON ZIP file from the specified URL. Then, employ the zipfile module, along with its limit method, to extract the data from the downloaded ZIP file. 


Proceed by creating an S3 bucket and generating a new IAM policy to grant permissions for AWS S3, Lambda, and CloudWatch to read and write data.


Next, establish a table in DynamoDB and configure a Lambda function with the assigned IAM role to trigger files from AWS S3 for storage in the DynamoDB table. Within the Lambda function, set up a trigger for the created S3 bucket and establish a connection between the S3 bucket and DynamoDB table. Convert the data from S3 into a dictionary format, and utilize the PUT function to store the data in the DynamoDB table.


Using AWS IAM, generate access and secret keys to connect AWS S3 locally via the boto3 method. With boto3, upload the downloaded JSON files to the S3 bucket.


Monitor the process through CloudWatch, and let Lambda trigger the S3 bucket to transfer its data to the DynamoDB table once uploaded.

