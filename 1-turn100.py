# tell when you will turn 100 years old
import datetime
today = datetime.date.today()
year = today.year

print(year)
print("This program tells you the year when you will turn 100")
name = input("Please, enter your name: ")
year_born = input("Now, enter the year you've been born: ")

age = year - int(year_born)
turn_100 = year + (100 - age)
print(f"{name} will turn 100 in {turn_100}")