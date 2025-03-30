import pandas as pd
import boto3
from db_connect import get_db_connection

# Function to fetch customer data and write to CSV
def fetch_customers():
    # Establish database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Execute the query
    cursor.execute("SELECT * FROM customer;")
    
    # Fetch the result
    result = cursor.fetchall()
    
    # Get column names (assuming the first row of the result is column names)
    columns = [desc[0] for desc in cursor.description]
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Create a DataFrame from the result set
    df = pd.DataFrame(result, columns=columns)
    
    # Write the result to a CSV file named 'mycustomers.csv'
    csv_filename = 'mycustomers.csv'
    df.to_csv(csv_filename, index=False)
    
    return csv_filename

# Function to upload the CSV to S3
def upload_to_s3(csv_filename, bucket_name, object_name):
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Upload the file
        s3_client.upload_file(csv_filename, bucket_name, object_name)
        print(f"File {csv_filename} uploaded successfully to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")

# Main logic
if __name__ == "__main__":
    # Fetch customer data and write to CSV
    csv_filename = fetch_customers()
    
    # S3 bucket information
    bucket_name = 'reportsgraphs'  # Replace with your bucket name
    object_name = 'mycustomers.csv'  # Define the desired object name in the S3 bucket

    # Upload the CSV to S3
    upload_to_s3(csv_filename, bucket_name, object_name)
