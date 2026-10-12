import json
with open("data/confidants.json") as f:
    data = json.load(f)
print(type(data))