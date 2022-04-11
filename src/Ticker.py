import json

stock_dict = {}
with open('stocks.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        split = line.split()
        stock_dict[split[1].lower()] = split[0]

json_object = json.dumps(stock_dict, indent = 4)
with open('company_to_ticker.json', 'w') as out_file:
    out_file.write(json_object)

print(stock_dict['tesla'])






