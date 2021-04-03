import requests


def delete_request(url, token, q=None):
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    try:
        delete_response = requests.delete(url, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        delete_response = ''
    if q:
        try:
            q.put(delete_response)
        except UnboundLocalError:
            q.put('ConnectionError')
    return delete_response
