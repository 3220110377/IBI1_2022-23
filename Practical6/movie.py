"""
First, import matplotlib.pyplot
Then, store and export the data as a dictionary
Finally, convert the data from dictionary to list format to create a pie chart
"""
import matplotlib.pyplot as plt
d = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18,
     'Documentary': 12, 'History': 8, 'War': 7}
print(d)  # store and export the data as a dictionary
values = list(d.values())
keys = list(d.keys())  # convert the data from dictionary to list format
# I drew this plot with the help of matplotlib official doc
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
plt.pie(values, labels=keys, autopct='%.2f%%')  # create a pie chart  # %.2f means two decimal places are retained
# %% means a % are added
plt.show()
"""
Suppose 'Horror' is entered, and the '19' represented by 'Horror' is output
"""
Input = 'Horror'
print(d[Input])
