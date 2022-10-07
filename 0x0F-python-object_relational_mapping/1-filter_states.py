#!/usr/bin/python3
"""  a script that lists all  states with a name starting with N (upper N)
from the database hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states LIKE (N%) ORDER BY id ASC;')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            print(row)

