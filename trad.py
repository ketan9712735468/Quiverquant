import os
import json

path = "/quiverquant/Senate/senatetrading_historical"


arr = os.listdir("quiverquant/Senate/senatetrading_historical")
arr.sort()
json_list = []

for i in arr:
    file = open(f"quiverquant/Senate/senatetrading_historical/{i}")
    data = json.load(file)
    json_list.append(data)


print(json_list)
# with open('master.json', 'w') as file_object:
#    json.dump(json_list, file_object)