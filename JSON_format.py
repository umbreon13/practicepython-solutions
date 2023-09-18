# JSON is a format to store data that can be stored and read by different languages
# keys can be lists, strings, booleans or other dictionaries
# for Python, you must use a dictionary or a list of dictionaries; also import json
# extension .json

#json validator: https://jsonlint.com/

import json   # necessary to store

info_about_me = {
"name": "Michele",
    "shirt_color": "blue",
    "laptops": [
    {
        "brand": "Lenovo",
        "operating_system": "Ubuntu"
    },
    {
        "brand": "Apple",
        "operating_system": "OSX"
    }
    ],
    "has_a_dog": False,
    "items_on_desk": ["mug", "pen", "monitor"]
}

# to store it in the same directory you are working in:
with open("info.json", "w") as f:
    json.dump(info_about_me, f)

## JSON won't store the name of the variable!! In this case, "info_about_me" disappears. It only stores the info inside.
# to solve this, I can load the info and store it in a new variable in this case, "info":

with open("info.json", "r") as f:
    info = json.load(f)

if info["has_a_dog"]:
    print("{} has a dog".format(info["name"]))
else:
    print("{} does not have a dog".format(info["name"]))