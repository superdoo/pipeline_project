import boto3
import pandas as pd

# Define the S3 client
s3_client = boto3.client('s3')

# Function to upload data to S3
def upload_to_s3():
    # Your logic to generate or fetch the data (e.g., from a DataFrame)
    data = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
    
    # Convert the DataFrame to CSV format
    csv_data = data.to_csv(index=False)
    
    # Define S3 bucket and object name
    bucket_name = 'reportsgraphs'
    object_name = 'resultset.csv'
    
    # Upload the CSV data to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_name,
        Body=csv_data
    )

# Call the upload function
upload_to_s3()
