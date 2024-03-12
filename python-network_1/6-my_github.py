#!/usr/bin/python3
import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script_name.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print("None")

if __name__ == "__main__":
    main()