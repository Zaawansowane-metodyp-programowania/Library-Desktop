import json

import requests
import urllib3


def get_request(url):
    urllib3.disable_warnings()
    resp = requests.get(url, verify=False)
    if resp.status_code != 200:
        print('Błąd')
    x = resp.json()
    result = json.dumps(x, indent=4)
    print(result)


if __name__ == '__main__':
    get_request('https://localhost:44340/api/users')
