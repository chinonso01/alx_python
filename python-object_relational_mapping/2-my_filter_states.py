import MySQLdb
import sys

def search_states(username, password, database, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query to retrieve states matching the given name (case-insensitive)
        query = "SELECT * FROM states WHERE name COLLATE utf8_general_ci = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()

        # Display states
        for state in states:
            print(state)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, database, state_name)
