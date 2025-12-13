import os
import glob
import yaml
import json
import logging
import requests
import datetime

# ---------------------------------------------------
# Task 3: Custom Exception (Robust Client Pattern)
# ---------------------------------------------------
class APIResponseError(Exception):
    """
    Custom exception for API 4xx/5xx errors with structured payload support.
    """
    def __init__(self, message, status_code, payload=None):
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload


# ---------------------------------------------------
# Task 2: Structured Logging (File + Console)
# (NO pythonjsonlogger)
# ---------------------------------------------------
def setup_logging():
    logger = logging.getLogger()

    # Clear handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.INFO)

    # JSON-style log format
    formatter = logging.Formatter(
        '{"time":"%(asctime)s","level":"%(levelname)s","message":"%(message)s"}'
    )

    # File handler
    file_handler = logging.FileHandler("project.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


logger = setup_logging()


# ---------------------------------------------------
# Robust API Client Pattern
# ---------------------------------------------------
class RobustClient:
    """
    Demonstrates a robust API client with proper error handling.
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
            logger.error(json.dumps({
                "event": "network_failure",
                "error": str(e)
            }))
            return None


# ---------------------------------------------------
# API Specification Analysis
# ---------------------------------------------------
def analyze_apis():
    files = glob.glob("specs/*.yaml")

    if not files:
        logger.error(json.dumps({
            "event": "no_yaml_files",
            "path": "specs/"
        }))
        return

    stats = {
        "total_endpoints": 0,
        "methods": {},
        "auth_methods": set(),
        "codes": {},
        "missing_responses": 0,
        "files_processed": 0
    }

    metadata = []

    logger.info(json.dumps({
        "event": "analysis_started",
        "file_count": len(files)
    }))

    for file_path in files:
        try:
            with open(file_path, "r") as f:
                data = yaml.safe_load(f)

            stats["files_processed"] += 1
            global_security = data.get("security", [])
            paths = data.get("paths", {})

            for path, methods in paths.items():
                for method, details in methods.items():
                    if method.lower() not in ["get", "post", "put", "delete", "patch"]:
                        continue

                    stats["total_endpoints"] += 1
                    method_upper = method.upper()
                    stats["methods"][method_upper] = stats["methods"].get(method_upper, 0) + 1

                    # Authentication logic
                    endpoint_security = details.get("security", global_security)
                    current_auth = []

                    if endpoint_security:
                        for rule in endpoint_security:
                            for scheme in rule.keys():
                                stats["auth_methods"].add(scheme)
                                current_auth.append(scheme)
                    else:
                        current_auth = ["None"]

                    # Response logic
                    responses = details.get("responses", {})
                    if not responses:
                        stats["missing_responses"] += 1

                    for code in responses:
                        stats["codes"][code] = stats["codes"].get(code, 0) + 1

                    metadata.append({
                        "file": os.path.basename(file_path),
                        "endpoint": path,
                        "method": method_upper,
                        "auth_methods": current_auth,
                        "response_codes": list(responses.keys())
                    })

            logger.info(json.dumps({
                "event": "file_parsed",
                "file": os.path.basename(file_path)
            }))

        except Exception as e:
            logger.error(json.dumps({
                "event": "file_parse_failed",
                "file": file_path,
                "error": str(e)
            }))

    # ---------------------------------------------------
    # Deliverables
    # ---------------------------------------------------

    # 1. Metadata JSON (overwrite)
    with open("metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    logger.info(json.dumps({
        "event": "metadata_written",
        "records": len(metadata)
    }))

    # 2. Summary Report (append)
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

    with open("README.txt", "a") as f:
        f.write(report)

    logger.info(json.dumps({
        "event": "summary_appended"
    }))

    print(report)


# ---------------------------------------------------
# Entry Point
# ---------------------------------------------------
if __name__ == "__main__":
    analyze_apis()
