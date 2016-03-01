import json

with open('./.tmp/localDiskDb.db') as data_file:
    data = json.load(data_file)

print(data["data"]["ports"][0]["source_ip"])
print(len(data["data"]["ports"]));
