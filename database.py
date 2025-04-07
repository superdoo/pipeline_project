import psycopg2
import pandas as pd

# Database connection settings
DB_CONFIG = {
    "dbname": "mbarreras_db",
    "user": "***********",
    "password": "*******",
    "host": "localhost",
    "port": "5432",
}


def fetch_customers():
    """Fetches customer data from my database and returns it as a Pandas DataFrame."""
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Execute query
        query = "SELECT * FROM customer;"
        cursor.execute(query)

        # Fetch results
        columns = [desc[0] for desc in cursor.description]  # Get column names
        rows = cursor.fetchall()

        # Convert to DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Close the connection
        cursor.close()
        conn.close()

        return df

    except Exception as e:
        print(f"Error fetching customers: {e}")
        return None


if __name__ == "__main__":
    df = fetch_customers()
    if df is not None:
        print(df.head())  # Print first few rows
