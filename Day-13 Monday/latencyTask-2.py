latency_data = [20, 35, 50, 15, 40, 60, 25]

def calculate_average(data):
    return sum(data) / len(data)

def get_summary(data):
    summary = {
        "Min": min(data),
        "Max": max(data),
        "Average": calculate_average(data)
    }
    return summary

print(f"Latency Summary: {get_summary(latency_data)}")