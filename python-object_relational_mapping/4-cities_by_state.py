import MySQLdb
import sys

def list_cities(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query to retrieve cities with their corresponding states
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                        JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
        cities = cursor.fetchall()

        # Display cities
        for city in cities:
            print(city)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
