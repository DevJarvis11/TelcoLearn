import subprocess
import json
import platform

routes = []
current_os = platform.system()

# ==============================
# WINDOWS LOGIC
# ==============================
if current_os == "Windows":
    print("Scanning Windows Routes...")
    # '-4' filters for IPv4 only, removing the messy IPv6 sections
    output = subprocess.getoutput("route print -4")
    
    for line in output.splitlines():
        parts = line.split()
        # Simple Filter: Valid route lines have exactly 5 columns and start with a number
        if len(parts) == 5 and parts[0][0].isdigit():
            routes.append({
                "route": parts[0],      # Destination
                "interface": parts[3],
                "protocol": "N/A",      # Not available in Windows output
                "source": parts[3],     # Usually same as interface
                "metric": parts[4]
            })

# ==============================
# LINUX LOGIC
# ==============================
elif current_os == "Linux":
    print("Scanning Linux Routes...")
    output = subprocess.getoutput("ip route show")
    
    for line in output.splitlines():
        parts = line.split()
        
        # Helper: Try to find a value after a keyword, or return "N/A"
        def get(keyword):
            return parts[parts.index(keyword) + 1] if keyword in parts else "N/A"

        routes.append({
            "route": parts[0],
            "interface": get("dev"),
            "protocol": get("proto"),
            "source": get("src"),
            "metric": get("metric")
        })

# ==============================
# SAVE & PRINT
# ==============================
# 1. Print to screen
print(json.dumps(routes, indent=4))

# 2. Save to file
filename = "routing_table.json"
try:
    with open(filename, "w") as f:
        json.dump(routes, f, indent=4)
    print(f"Success! Saved to {filename}")
except Exception as e:
    print(f"Error saving file: {e}")