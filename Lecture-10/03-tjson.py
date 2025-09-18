import json

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))
print(f'name: {parsed_data["name"]}, age: {parsed_data["age"]}')