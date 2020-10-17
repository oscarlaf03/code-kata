import json
file = open('data.json')

data = json.load(file)['transactions']
test = data[9]
print(test)

# for row in data["transactions"]:
#     print(row)

