import boto3
import json

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
        # fetch bucket name from event json object
        bucket = event['Records'][0]['s3']['bucket']['name']
        print("bucket_name = " + bucket)
        # fetch file name which is uploaded in s3 bucket from event json object
        json_file_name = event['Records'][0]['s3']['object']['key']
        print("file_name = " + json_file_name)
        #Lets call get_object() function which Retrieves objects from Amazon S3 as dictionary
        json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
        print("before_decoding"+str(type(json_object)))
        # Lets decode the json object returned by function which will retun string
        file_reader = json_object['Body'].read().decode("utf-8")
        print(type(file_reader))
        print(file_reader)
        # Convert JSON string to dictionary
        file_reader_dict = json.loads(file_reader)
        print(type(file_reader_dict))
        print(file_reader_dict)
        # As we have retrieved the dictionary we will put it in DynamoDB table
        table = dynamodb.Table('tabletest8940')
        table.put_item(Item=file_reader_dict)
        return 'success'
