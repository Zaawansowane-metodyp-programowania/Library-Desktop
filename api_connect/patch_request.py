import json

import requests


def patch_request(url: str, data: dict, token: str, q=None):
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


# if __name__ == '__main__':
#     response = patch_request('https://library-api-app.azurewebsites.net/api/users/changePassword/58', {
#         "oldPassword": "963147",
#         "newPassword": "963147",
#         "confirmNewPassword": "963147"
#     },
#                              'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjU4IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6Ikpha3ViIExpb2hlYXJ0IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiVXNlciIsImV4cCI6MTYxODM4ODAwOCwiaXNzIjoiaHR0cDovL2xpYnJhcnlhcGkuY29tIiwiYXVkIjoiaHR0cDovL2xpYnJhcnlhcGkuY29tIn0.9WeqeFOlKmIHuqQtDUXCYE3Rj2JJL9QmW2FcLlgQaRs')
#     print(type(response))
#     print(response)
