import json

BASELINE_FILE = "baseline.json"

def save_baseline(data):
    with open(BASELINE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_baseline():
    with open(BASELINE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)