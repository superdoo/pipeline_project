import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import BytesIO
from db_connect import get_db_connection

# S3 Configuration
BUCKET_NAME = "your-s3-bucket-name"  # Replace with your bucket name

def fetch_album_data():
    """Fetch album data from the database and save it as a CSV file."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT al.*
    FROM artists a
    JOIN albums al ON a.artist_id = al.artist_id;
    """
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Get column names
    columns = [desc[0] for desc in cursor.description]

    # Convert to DataFrame
    df = pd.DataFrame(result, columns=columns)

    # Save to CSV
    csv_filename = "album_data.csv"
    df.to_csv(csv_filename, index=False)
    
    cursor.close()
    conn.close()

    print(f"CSV file saved: {csv_filename}")
    return csv_filename, df

def create_graph(df):
    """Generate a bar chart showing album counts per artist."""
    album_counts = df["artist_id"].value_counts()

    plt.figure(figsize=(10, 5))
    album_counts.plot(kind="bar", color="skyblue")
    plt.xlabel("Artist ID")
    plt.ylabel("Number of Albums")
    plt.title("Albums per Artist")
    plt.xticks(rotation=45)

    graph_filename = "album_graph.png"
    plt.savefig(graph_filename)
    plt.close()

    print(f"Graph saved: {graph_filename}")
    return graph_filename

def upload_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket."""
    s3_client = boto3.client("s3")
    if object_name is None:
        object_name = file_name

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Uploaded {file_name} to S3 bucket {bucket} as {object_name}")
    except Exception as e:
        print(f"Error uploading {file_name} to S3: {e}")

if __name__ == "__main__":
    csv_file, df = fetch_album_data()
    graph_file = create_graph(df)

    # Upload files to S3
    upload_to_s3(csv_file, BUCKET_NAME)
    upload_to_s3(graph_file, BUCKET_NAME)
