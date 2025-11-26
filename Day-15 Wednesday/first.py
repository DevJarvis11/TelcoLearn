#-------------------------------------------------

# import json

# with open("titanic.json") as f:
#     data = json.load(f)

# print(data["passengers"])

#-------------------------------------------------

# import json

# with open("capture.json") as f:
#     data = json.load(f)


# print(data[0]["_source"])


#-------------------------------------------------


# import yaml

# with open("docker.yaml") as f:
#     data = yaml.safe_load(f)

# for item in data["services"]["oai-amf"]["environment"]:
#     if "MCC=" in item:
#         print(item.split('=')[1])


#-------------------------------------------------


# import yaml

# with open("docker.yaml") as f:
#     data = yaml.safe_load(f)

# for item in data["services"]["oai-amf"]["environment"]:
#     if "=" in item and item.count('.') == 3:
#         print(item.replace('=', ': '))


#-------------------------------------------------

# import yaml


# with open("docker.yaml") as f:
#     data = yaml.safe_load(f)


# for service, config in data["services"].items():
#     for item in config.get("environment", []):
#         if "PORT" in item and "=" in item:
#             print(f"[{service}]", item.replace('=', ': '))


#-------------------------------------------------

# import yaml

# with open("docker.yaml") as f:
#     data = yaml.safe_load(f)

# for name, config in data["services"].items():

#     list = config.get("environment", [])

#     for item in list:
#         if "NRF_PORT" in item and "=" in item:
#             print(f"[{name}]", item.replace("=", ": "))


#-------------------------------------------------

import yaml  # Requires: pip install PyYAML
import json

# 1. Load the YAML file
try:
    with open("CommonData.yaml", "r") as yaml_file:
        # Load the YAML content into a Python Dictionary
        data = yaml.safe_load(yaml_file)

    # 2. Save as a JSON file
    with open("CommonData.json", "w") as json_file:
        # dump converts the dictionary to a JSON string
        json.dump(data, json_file, indent=4)

    print("Converted 'CommonData.yaml' to 'CommonData.json'")
    
    # Optional: Print the first few lines to the console to verify
    print("\n--- JSON OUTPUT PREVIEW ---")
    print(json.dumps(data, indent=4)[:500] + "\n...")

except FileNotFoundError:
    print("Error: The file 'CommonData.yaml' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")