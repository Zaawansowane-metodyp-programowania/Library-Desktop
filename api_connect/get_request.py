import requests
import urllib3


def get_request(url, token, q=None):
    urllib3.disable_warnings()
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}
    resp = requests.get(url, headers=headers, verify=False)
    if resp.status_code != 200:
        print('Błąd')
    get_response = resp.json()
    if q:
        q.put(get_response)
    return get_response


if __name__ == '__main__':
    response = get_request('https://library-api-app.azurewebsites.net/api/users',
                           'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjM0IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6ImFkbWluIGFkbWluIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQWRtaW4iLCJleHAiOjE2MTgyOTYxOTksImlzcyI6Imh0dHA6Ly9saWJyYXJ5YXBpLmNvbSIsImF1ZCI6Imh0dHA6Ly9saWJyYXJ5YXBpLmNvbSJ9.Lx50-mqxvuJgE5UpRXEtLPwrMfOLeOmMMVZFbcmL374')
    print(response)
