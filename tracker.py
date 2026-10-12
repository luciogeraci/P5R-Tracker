import json
with open("data/confidants.json") as f:
    data = json.load(f)
for c in data["confidants"]:
    print(c["name"], c["arcana"], c["unlock"]["date"])