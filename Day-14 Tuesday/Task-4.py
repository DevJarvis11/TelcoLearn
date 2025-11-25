import requests
import logging

# -----------------------------------
# STEP 1: Configure Logging
# -----------------------------------
logging.basicConfig(
    filename="app2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------
# STEP 2: Decorator to auto-log calls
# -----------------------------------
def log_calls(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function called: {func.__name__} | Args: {args} | Kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# -----------------------------------
# STEP 3: API Function (auto-logged)
# -----------------------------------
@log_calls
def fetch_api(url):
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except Exception:
        return None    # keeps it simple

# -----------------------------------
# STEP 4: Test functions
# -----------------------------------
for label, url in [
    ("GOOD", "https://jsonplaceholder.typicode.com/todos/1"),
    ("BAD", "https://invalid-example-123.com")
]:
    print(f"\nTesting {label} URL:")
    print(fetch_api(url))
