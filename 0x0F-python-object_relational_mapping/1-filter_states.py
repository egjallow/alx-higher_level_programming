#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
