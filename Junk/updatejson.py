import json

with open("data.json", "r") as jsonFile:
    data = json.load(jsonFile)
    ref = data["userdata"][0]
    ref["Password"] = "123456"

with open("data.json", "w") as jsonFile:
    json.dump(data, jsonFile)
