import sys
import MySQLdb

def list_cities(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the query
    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))
    
    # Fetch all results
    cities = cursor.fetchall()
    
    # Print the results
    print(", ".join(city[0] for city in cities))
    
    # Close cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    list_cities(username, password, database, state_name)
