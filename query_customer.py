import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import boto3
from db_connect import get_db_connection

def fetch_album_genre_data():
    """
    Fetch artist, album, and genre data from the database.
    """
    # Open a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute the query to fetch artist name, album name, and genre
    cursor.execute("""
        SELECT a.name, al.title, ag.name
        FROM artists a
        JOIN albums al ON a.artist_id = al.artist_id
        JOIN genres ag on ag.genre_id = al.genre_id; 
    """)

    # Fetch the results
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert the result into a pandas DataFrame
    df = pd.DataFrame(result, columns=["Artist", "Album", "Genre"])
    return df

def plot_genre_distribution(df):
    """
    Plot the distribution of albums by genre and save the plot as an image.
    """
    # Count the number of albums per genre
    genre_counts = df["Genre"].value_counts()

    # Plot the distribution of genres
    plt.figure(figsize=(10, 6))
    genre_counts.plot(kind='bar', color='skyblue')
    plt.title("Album Distribution by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Number of Albums")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image
    plot_filename = 'album_genre_distribution.png'
    plt.savefig(plot_filename)
    plt.close()

    return plot_filename

def upload_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.
    """
    # If no object name is provided, use the file name
    if object_name is None:
        object_name = file_name

    # Upload the file to S3
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded to S3 bucket {bucket_name} as {object_name}.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def main():
    """
    Main function to fetch data, generate the plot, and upload the plot to S3.
    """
    # Fetch the album genre data
    df = fetch_album_genre_data()

    # Plot the genre distribution graph
    plot_filename = plot_genre_distribution(df)

    # Define your S3 bucket name
    bucket_name = 'reportsgraphs'

    # Upload the plot to S3
    upload_to_s3(plot_filename, bucket_name)

if __name__ == "__main__":
    main()
