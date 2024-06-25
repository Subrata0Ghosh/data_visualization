import pymysql

def get_connection():
    """
    Establishes a connection to the MySQL database.
    Replace the placeholders with your actual database credentials.
    """
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='data_visualization',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def get_data_from_database():
    """
    Fetches data from the database and returns it.
    You'll need to replace this with your actual query logic.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Example query: Fetch data from a table
            sql = "SELECT * FROM EnergyForecasts"
            cursor.execute(sql)
            data = cursor.fetchall()
    finally:
        connection.close()
    
    return data
