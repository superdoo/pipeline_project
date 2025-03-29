import boto3
import json
import os
from query_customer import fetch_customers

def upload_to_s3():
    # Get the AWS credentials from environment variables (set in Jenkins)
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    # Initialize boto3 client using the credentials from environment variables
    s3_client = boto3.client(
        's3', 
        aws_access_key_id=aws_access_key_id, 
        aws_secret_access_key=aws_secret_access_key
    )
    
    data = fetch_customers()
    json_data = json.dumps(data)

    # Upload to S3
    s3_client.put_object(
        Bucket='reportsgraphs',
        Key='customer_data.json',
        Body=json_data
    )

if __name__ == "__main__":
    upload_to_s3()
