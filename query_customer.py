import pandas as pd
from db_connect import get_db_connection

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
    df.to_csv('mycustomers.csv', index=False)
    
    # Optionally, return the DataFrame if needed for further processing
    return df
