import requests


def get_request(url, token, q=None):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print('Błąd')
    print(resp)
    get_response = resp.json()
    if q:
        q.put(get_response)
    return get_response
