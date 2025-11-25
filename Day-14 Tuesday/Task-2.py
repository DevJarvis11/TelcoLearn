import requests

class APIResponseError(Exception): pass

def fetch(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            raise APIResponseError("Bad status code")
        return r.json()
    except Exception as e:
        raise APIResponseError(e)

for url in [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://wrong-url-12345.com"
]:
    try:
        print(fetch(url))
    except APIResponseError as e:
        print("Error:", e)