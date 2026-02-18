# JSON Practice

import json

# 1. Python to JSON
data = {
    "name": "Ali",
    "age": 20,
    "is_student": True,
    "courses": ["Python", "Math", "AI"]
}

json_string = json.dumps(data, indent=4)
print("JSON string:")
print(json_string)

# 2. JSON to Python
parsed = json.loads(json_string)
print("\nParsed name:", parsed["name"])

# 3. Write JSON to file
with open("sample-data.json", "w") as file:
    json.dump(data, file, indent=4)

# 4. Read JSON from file
with open("sample-data.json", "r") as file:
    loaded_data = json.load(file)

print("\nLoaded from file:", loaded_data)
