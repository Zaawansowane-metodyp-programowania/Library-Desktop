import json

import requests


class InvalidLoginOrPassError(Exception):
    def __str__(self):
        return 'Niepoprawne dane logowania'


def post_request(url, data, token=None, q=None):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    if token:
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}
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
