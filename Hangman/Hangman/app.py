import pyodbc

def get_word_list(username, password):
    # Connect to the SQL server
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=MSI;'
                          'Database=Hangman;'
                          'UID=' + username + ';PWD=' + password)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query to retrieve the list
    cursor.execute("SELECT Word FROM tWords")

    # Fetch all the results into a list
    word_list = [row[0] for row in cursor.fetchall()]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return word_list