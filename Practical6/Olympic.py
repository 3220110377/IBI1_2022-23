"""
First, import matplotlib.pyplot and numpy
Then, store and export the data as two lists
Finally, create a bar chart
"""
import numpy as np
import matplotlib.pyplot as plt
N = 8
costs = [1, 8, 15, 7, 5, 14, 43, 40]
time = ['1984', '1988', '1992', '1996', '2000', '2003', '2008', '2012']
new = sorted(costs)  # Sort the data from largest to smallest and call it new
print(new)
ind = np.arange(N)  # make array from 0 to 7
p = plt.bar(ind, costs, 0.3)
plt.ylabel('cost')  # y-axis name
plt.title('olympic cost')  # the title of the chart
plt.xticks(ind, np.array(time))
plt.yticks(np.arange(0, 50, 5))  # The y axis is scaled from 0 to 50 at intervals of 5
plt.show()
# I drew this plot with the help of https://blog.csdn.net/mighty13/article/details/113869911
