import json

import requests


def put_request(url, data, token, q=None):
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    app_json = json.dumps(data)
    try:
        put_response = requests.put(url, data=app_json, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        put_response = ''
    if q:
        try:
            q.put(put_response)
        except UnboundLocalError:
            q.put('ConnectionError')
    return put_response
