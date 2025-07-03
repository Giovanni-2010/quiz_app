import json

# 1. Read the .txt file
with open('questions.txt', 'r', encoding='utf-8') as txt_file:
    data = txt_file.read()

# 2. Convert the string content to a Python object
try:
    json_data = json.loads(data)
except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
    exit()

# 3. Write the data to a .json file
with open('questions.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print("File saved as 'questions.json'")
