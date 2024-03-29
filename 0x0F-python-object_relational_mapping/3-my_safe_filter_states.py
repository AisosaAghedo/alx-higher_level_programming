#!/usr/bin/python3
"""  that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd='password',
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('''SELECT * FROM states WHERE states.name
                LIKE %s ORDER BY id ASC;''', (argv[4],))
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            print(row)
