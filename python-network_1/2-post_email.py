#!/usr/bin/python3
import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script_name.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)

if __name__ == "__main__":
    main()
