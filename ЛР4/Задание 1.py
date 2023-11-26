import json
def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        data = json.load(f)

    total = sum(item["score"] * item["weight"] for item in data)
    return round(total, 3)

print(task())
