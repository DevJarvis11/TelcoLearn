import requests
import logging

# Step 1 & 3: Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 2 & 4: API function with logging
def fetch_data(url):
    logging.info(f"Fetching: {url}")

    try:
        data = requests.get(url, timeout=5).json()
        logging.info("Success")
        return data

    except Exception as e:
        logging.error(f"Error: {e}")
        print("Error:", e)
        return None

# Step 5: Test the function
for label, url in [
    ("GOOD", "https://jsonplaceholder.typicode.com/todos/1"),
    ("BAD", "https://invalid-example-123.com")
]:
    print(f"\nTesting {label} URL:")
    print(fetch_data(url))
