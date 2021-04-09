import requests


def delete_request(url, token, q=None):
    """
    Funkcja obsługująca API DELETE. Wymaga podania url, tokena użytkownika oraz opcjonalnego parametru q do
    obsługi wielowątkowości.
    :param url: str
    :param token: str
    :param q: object
    :return: json
    """
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
