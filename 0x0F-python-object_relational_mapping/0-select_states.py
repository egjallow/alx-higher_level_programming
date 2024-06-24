#!/usr/bin/python3
"""Lits all state from the databse hbtn_0e_0_usa"""

if __name__== '__main__':
    from sys import argv
    import MySQLdb


    conn = MySQLdb.connect(host='localhost', port=3306,user=argv[1], passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute('SELECT * FROM states ORDER BY id ASC')
    rows = c.fetchall()

    for state in rows:
        print(state)
    c.close()
    conn.close()
