#!/usr/bin/python3
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(request_id)
    else:
        print("None")

if __name__ == "__main__":
    main()
