import yaml


with open("docker.yaml") as f:
    data = yaml.safe_load(f)


for service, config in data["services"].items():
    for item in config.get("environment", []):
        if "PORT" in item and "=" in item:
            print(f"[{service}]", item.replace('=', ': '))