import os
import pyodbc

# Accessing the environment variables
sql_server_host = os.getenv('SQL_SERVER_HOST_QA')
sql_server_db = os.getenv('SQL_SERVER_DB_QA')
sql_server_user = os.getenv('SQL_SERVER_USER_QA')
sql_server_pass = os.getenv('SQL_SERVER_PASS_QA')
sql_server_driver = os.getenv('SQL_SERVER_DRIVER_QA')


# Create the connection string using the retrieved environment variables
connection_string = (
    f"DRIVER={sql_server_driver};"
    f"SERVER={sql_server_host};"
    f"DATABASE={sql_server_db};"
    f"UID={sql_server_user};"
    f"PWD={sql_server_pass};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# Connect to the SQL Server database
try:
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Query to fetch data from the dbo.issue table
    cursor.execute("SELECT * FROM table")

    # Fetch all results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

except Exception as e:
    print("Error connecting to the database:", e)
finally:
    # Close the connection
    if 'connection' in locals():
        connection.close()
