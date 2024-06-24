#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    name = argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    c = conn.cursor()
    c.execute(("SELECT * FROM states "
               "WHERE name='{}' "
               "ORDER BY id".format(name)))

    rows = c.fetchall()

    for row in rows:
        print(row)
