import os
import glob
import yaml
import json
import logging
import requests
import datetime
from pythonjsonlogger import jsonlogger

# --- Task 3: Custom Exception (Robust Client Pattern) ---
class APIResponseError(Exception):
    """
    Custom exception for API 4xx/5xx errors with structured payload support.
    """
    def __init__(self, message, status_code, payload=None):
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload

# --- Task 2: Structured Logging Setup (File + Console) ---
def setup_logging():
    logger = logging.getLogger()
    
    # Clear existing handlers to avoid duplicates on re-runs
    if logger.hasHandlers():
        logger.handlers.clear()
        
    logger.setLevel(logging.INFO)
    
    # Define the JSON formatter
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')

    # 1. File Handler (Stores logs in project.log)
    file_handler = logging.FileHandler('project.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 2. Stream Handler (Optional: Prints logs to terminal as well)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

logger = setup_logging()

# --- Robust Client Pattern ---
class RobustClient:
    """
    Demonstrates the required 'Robust API Client Pattern'.
    """
    def fetch_spec(self, url):
        try:
            response = requests.get(url, timeout=10)
            if 400 <= response.status_code < 600:
                raise APIResponseError(
                    f"API Error {response.status_code}", 
                    response.status_code, 
                    payload=response.text
                )
            return response.text
        except requests.RequestException as e:
            logger.error(f"Network failed: {str(e)}")
            return None

def analyze_apis():
    # 1. Locate files in the existing 'specs' folder
    files = glob.glob("specs/*.yaml")
    
    if not files:
        logger.error("No YAML files found in 'specs/' folder.")
        return

    stats = {
        "total_endpoints": 0,
        "methods": {},
        "auth_methods": set(),
        "codes": {},
        "missing_responses": 0,
        "files_processed": 0
    }

    logger.info(f"Starting analysis", extra={"file_count": len(files)})
    metadata = []

    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)

            stats["files_processed"] += 1
            global_security = data.get('security', [])
            
            paths = data.get('paths', {})
            for path, methods in paths.items():
                for method, details in methods.items():
                    if method.lower() not in ['get', 'post', 'put', 'delete', 'patch']: continue

                    stats["total_endpoints"] += 1
                    stats["methods"][method.upper()] = stats["methods"].get(method.upper(), 0) + 1
                    
                    # Auth Logic
                    endpoint_security = details.get('security', global_security)
                    current_auth = []
                    if endpoint_security:
                        for sec_rule in endpoint_security:
                            for scheme_name in sec_rule.keys():
                                stats["auth_methods"].add(scheme_name)
                                current_auth.append(scheme_name)
                    else:
                        current_auth = ["None"]

                    # Response Logic
                    responses = details.get('responses', {})
                    if not responses:
                        stats["missing_responses"] += 1
                    
                    for code in responses:
                        stats["codes"][code] = stats["codes"].get(code, 0) + 1

                    metadata.append({
                        "file": os.path.basename(file_path),
                        "endpoint": path,
                        "method": method.upper(),
                        "auth_methods": current_auth,
                        "response_codes": list(responses.keys())
                    })
            
            logger.info(f"Parsed file successfully", extra={"file": os.path.basename(file_path)})

        except Exception as e:
            logger.error(f"Failed to parse file", extra={"file": file_path, "error": str(e)})

    # --- Deliverables ---
    
    # 1. JSON Metadata Dump (Overwrites previous run)
    with open("metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    logger.info("Metadata saved to metadata.json")

    # 2. Summary Report (APPENDS to README.txt)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"""
    
    ========================================
    RUN SUMMARY - {timestamp}
    ========================================
    Total Files Parsed: {stats['files_processed']}
    Total Endpoints: {stats['total_endpoints']}
    Methods Distribution: {json.dumps(stats['methods'], indent=2)}
    Response Codes Observed: {json.dumps(stats['codes'], indent=2)}
    Authentication Methods: {list(stats['auth_methods'])}
    Endpoints with No Response Definition: {stats['missing_responses']}
    ========================================
    """
    
    # Using "a" mode for append
    with open("README.txt", "a") as f:
        f.write(report)
    
    logger.info("Summary report appended to README.txt")
    print(report)

if __name__ == "__main__":
    analyze_apis()