#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # Connect to the database
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Create a cursor object
    c = conn.cursor()

    # Execute the SQL query to find states with names starting with 'N'
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results
    rows = c.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    c.close()
    conn.close()
