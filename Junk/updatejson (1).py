import json

with open("data.json", "r") as jsonFile:
    data = json.load(jsonFile)
    userid = input("Please enter your id")
    filtered = list(filter(lambda f: (f["id"] == userid), data["userdata"]))
    newpass = input("Enter new password")
    filtered[0]["Password"] = newpass


with open("data.json", "w") as jsonFile:
    json.dump(data, jsonFile)
