# need to import at least 3 things to make your
# bokeh plots work
from bokeh.plotting import figure, show, output_file

# we specify an HTML file where the output will go
output_file("plot.html")

## load our x and y data
# x1 = [10, 20, 30]  # for numerical variables

x_categories = ["a", "b", "c", "d", "e"]  # categorical values (strings)
x2 = ["a", "d", "e"]

y = [4, 5, 6]

## create a figure
# p = figure()
q = figure(x_range=x_categories)  # what is going to be printed

# create a histogram
# p.vbar(x=x1, top=y, width=0.5)  # data
q.vbar(x=x2, top=y, width=0.5)

# render (show) the plot
show(q)