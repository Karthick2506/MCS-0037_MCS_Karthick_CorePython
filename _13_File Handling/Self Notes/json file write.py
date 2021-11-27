import json

# Data to be written
dictionary = {
    "name": "Karthick",
    "rollno": 55,
    "cgpa": 8.6,
    "phonenumber": "8955353565"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample2.json", "w") as outfile:
    outfile.write(json_object)

