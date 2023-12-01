#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    query = argv[1] if len(argv) > 1 else ''
    data = {
        'q': f'{query}'
        }

    try:
        response = requests.post(url, data=data).json()
        if response == {}:
            print('No result')
        else:
            print(f"[{response.get('id')}] {response.get('name')}")

    except ValueError as json_error:
        print('Not a valid JSON')
