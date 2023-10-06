# extract the birth months and count how many scientists were born in each month

import json
from collections import Counter  #imports the counter function, NOT USED

with open("birthdays.json", "r") as file:
    bday = json.load(file)

list_mth = ["-","January","February","March","April","May","June","July","August","September","October","November","December"]
output_dic = {}

for elem in bday:
    x = bday[elem]
    n_month = int(x[3:5])  # takes the month number, positions 3 and 4 in the string
    month = list_mth[n_month]
    if month in output_dic:
        output_dic[month] += 1
    else:
        output_dic[month] = 1
    
print(output_dic)
