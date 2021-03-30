import json

import requests


class InvalidLoginOrPassError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Niepoprawne dane logowania'


def post_request(url, data, q=None):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    app_json = json.dumps(data)
    try:
        post_response = requests.post(url, data=app_json, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        post_response = ''
    if q:
        try:
            q.put(post_response)
        except UnboundLocalError:
            q.put('ConnectionError')
    return post_response


if __name__ == '__main__':
    response = post_request('https://library-api-app.azurewebsites.net/api/account/login', {
        "email": "admin@example.com",
        "password": "admin1"
    })
    print(type(response))
