import json

json_data = '{"name": "John Smith", "age": 30, "city": "New York"}'

# parse json_data
parsed_json = json.loads(json_data)

# print the parsed json
print(parsed_json)