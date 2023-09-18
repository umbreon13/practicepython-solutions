import json

# store info
# bday = {
#     "Albert Einstein": "17/01/1706",
#     "Benjamin Franklin": "14/04/1879",
#     "Ada Lovelace": "10/12/1815",
# }

with open("birthdays.json", "r") as file:
    bday = json.load(file)

# print(f"We've got these birthdays: {bday.keys()}")
userin = input("Which one do you want to know? ")

output = bday.get(userin, "This person is not in the list")  #2nd arg if it's not in the list

while output == "This person is not in the list":
    print(output)
    # print(f"We've got these birthdays: {bday.keys()}")
    userin = input("Which one do you want to know? (Type 'quit' to exit): ")
    output = bday.get(userin, "This person is not in the list")
    if userin == "quit":
        break

print(f"{userin}'s birthday is on {output}")

# introduce a new scientific
intro_new = input("Do you want to introduce a new scientific birthday? (yes/no) ")
if intro_new.lower() == "yes":
    in_name = input("Please, introduce the name (e.g.: Albert Einstein): ")
    in_day = input("Now, introduce the date (dd/mm/yyy): ")
    bday[in_name] = in_day
else:
    print("")

with open("birthdays.json", "w") as file:
    json.dump(bday, file)