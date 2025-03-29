from query_customer import fetch_customer_data
from upload_s3 import upload_to_s3

def main():
    file_name = fetch_customer_data()
    if file_name:
        upload_to_s3(file_name)

if __name__ == "__main__":
    main()
