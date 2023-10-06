# extract the birth months and plot

# need to import at least 3 things to make your
# bokeh plots work
from bokeh.plotting import figure, show, output_file

# we specify an HTML file where the output will go
output_file("plot.html")

import json

# extract data
with open("birthdays.json", "r") as file:
    bday = json.load(file)

list_mth = ["-","January","February","March","April","May","June","July","August","September","October","November","December"]
output_dic = {}
# output_dic = {"January":0,"February":0,"March":0,
#               "April":0,"May":0,"June":0
#               ,"July":0,"August":0,"September":0,"October":0,"November":0,"December":0}

for elem in bday:
    n = bday[elem]
    n_month = int(n[3:5])  # takes the month number, positions 3 and 4 in the string
    month = list_mth[n_month]
    if month in output_dic:
        output_dic[month] += 1
    else:
        output_dic[month] = 1
    
print(output_dic)

# we specify an HTML file where the output will go
output_file("plot.html")

# x,y data
x_categories = list_mth[1:]
x = list(output_dic.keys())  # this has to be a list!!!
y = list(output_dic.values())

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

# print(x_categories)
# print(x)
# print(y)
show(p)