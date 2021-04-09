import json

import requests


def patch_request(url: str, data: dict, token: str, q=None):
    """
    Funkcja obsługująca API PATCH. Wymaga podania url, tokena użytkownika, danych w formacie doc oraz opcjonalnego
    parametru q do obsługi wielowątkowości.
    :param url: str
    :param data: doc
    :param token: str
    :param q: object
    :return: json
    """
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    app_json = json.dumps(data)
    try:
        post_response = requests.patch(url, data=app_json, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        raise e
    if q:
        q.put(post_response)
    return post_response.status_code
