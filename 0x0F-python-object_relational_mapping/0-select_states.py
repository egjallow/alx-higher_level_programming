#!.usr/bin/python3
"""Lits all state from the databse hbtn_0e_0_usa"""

if __name__== '__main__':
    from sys import argv
    import MySQLdb


    conn = MySQLdb.connect(host='localhost', port=3306,user=argv[1], passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute('SELECT * FROM states')

    rows = c.fetchall()

    for i in rows:
        print(i)
