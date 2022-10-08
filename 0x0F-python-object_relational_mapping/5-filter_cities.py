#!/usr/bin/python3
"""  a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd='password',
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))
    result = cur.fetchall()
    print(", ".join(city[0] for city in result))
    cur.close()
    db.close()
