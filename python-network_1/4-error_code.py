#!/usr/bin/python3
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

if __name__ == "__main__":
    main()