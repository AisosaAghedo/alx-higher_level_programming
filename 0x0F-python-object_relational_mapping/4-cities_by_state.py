#!/usr/bin/python3
"""  a script that lists all cities from the database hbtn_0e_4_usa """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('''SELECT cities.id, cities.name, states.name FROM states
                JOIN cities ON states.id=cities.state_id; ''')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            print(row)
