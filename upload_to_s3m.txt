from database import fetch_customers  # Ensure this matches the correct file name

def upload_to_s3():
    data = fetch_customers()  # This should now work
    print("Uploading data:", data)
    # Add S3 upload logic here
        # Upload to S3
    s3_client.put_object(
        Bucket='reportsgraphs',
        Key='customer_data.json',
        Body=json_data
    )

if __name__ == "__main__":
    upload_to_s3()
