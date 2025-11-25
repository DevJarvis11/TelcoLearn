import requests

def fetch_data(url):
    try:
        return requests.get(url, timeout=5).json()
    except Exception as e:
        print("Error:", e)
        return None

for label, url in [
    ("GOOD", "https://jsonplaceholder.typicode.com/todos/1"),
    ("BAD", "https://invalid-example-123.com")
]:
    print(f"\nTesting {label} URL:")
    print(fetch_data(url))