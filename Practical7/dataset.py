import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/ibi/IBI1_2022-23/Practical7")  # Change the working directory
print(os.getcwd())  # Show the working directory
print(os.listdir())  # List the file under the directory
covid_data = pd.read_csv("full_data.csv")  # Use pandas to read the csv file

print(covid_data.head(5))  # Output the first five columns of the file
# 5 means the first five columns of the file
"""
         date     location  new_cases  new_deaths  total_cases  total_deaths
0  2019-12-31  Afghanistan          0           0            0             0
1  2020-01-01  Afghanistan          0           0            0             0
2  2020-01-02  Afghanistan          0           0            0             0
3  2020-01-03  Afghanistan          0           0            0             0
4  2020-01-04  Afghanistan          0           0            0             0
"""
print(covid_data.info())  # There are six rows and "data" and "location" is object type,
# "new_cases", "new_deaths", "total_cases" and "total_deaths" is int64 type
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7996 entries, 0 to 7995
Data columns (total 6 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   date          7996 non-null   object
 1   location      7996 non-null   object
 2   new_cases     7996 non-null   int64 
 3   new_deaths    7996 non-null   int64 
 4   total_cases   7996 non-null   int64 
 5   total_deaths  7996 non-null   int64 
dtypes: int64(4), object(2)
memory usage: 374.9+ KB
"""
print(covid_data.describe())  # Show the number of entries, mean, standard deviation and a number of quantiles.
# the mean of new cases is 194.546773 and the standard deviation is 2083.395028
# total cases from 0.000000 to 777798.000000
"""
None
          new_cases   new_deaths    total_cases  total_deaths
count   7996.000000  7996.000000    7996.000000   7996.000000
mean     194.546773     9.322661    2441.369060     97.977239
std     2083.395028   108.183439   22375.617031   1023.038977
min       -9.000000     0.000000       0.000000      0.000000
25%        0.000000     0.000000       0.000000      0.000000
50%        0.000000     0.000000       3.000000      0.000000
75%        8.000000     0.000000      60.000000      0.000000
max    65162.000000  3698.000000  777798.000000  37272.000000
"""
print(covid_data.iloc[0, 1])
print(covid_data.location.head(1))  # check it by head
"""
Afghanistan
"""
"""
0    Afghanistan
Name: location, dtype: object
"""
print(covid_data.iloc[2, 0:5])  # row 2 and column 0 to 5
"""
date            2020-01-02
location       Afghanistan
new_cases                0
new_deaths               0
total_cases              0
Name: 2, dtype: object
"""
print(covid_data.iloc[0:2, :])  # row 0 to 2 and all column
"""
        date     location  new_cases  new_deaths  total_cases  total_deaths
0  2019-12-31  Afghanistan          0           0            0             0
1  2020-01-01  Afghanistan          0           0            0             0
"""
print(covid_data.iloc[0:10:2, 0:5])  # row 0 to 10 step is 2 and column 0 to 5
"""
         date     location  new_cases  new_deaths  total_cases
0  2019-12-31  Afghanistan          0           0            0
2  2020-01-02  Afghanistan          0           0            0
4  2020-01-04  Afghanistan          0           0            0
6  2020-01-06  Afghanistan          0           0            0
8  2020-01-08  Afghanistan          0           0            0
"""
print(covid_data.iloc[0:1001:100, 2])  # the answer of the question
"""
0        0
100     28
200     13
300      0
400      0
500      0
600      2
700      2
800      0
900      0
1000     4
Name: new_cases, dtype: int64
"""
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3, my_columns])  # True is the column be chosen and False is the column not be chosen
"""
         date     location  new_deaths
0  2019-12-31  Afghanistan           0
1  2020-01-01  Afghanistan           0
2  2020-01-02  Afghanistan           0
"""
# print(covid_data.iloc[0:3, [True, True, False, True, False]])
# print(covid_data.iloc[0:3, [True, True, False, True, False, False, True]])
# Both of them get error

print(covid_data.loc[2:4, "date"])
"""
2    2020-01-02
3    2020-01-03
4    2020-01-04
Name: date, dtype: object
"""
boolean_list = list()
for i in covid_data.loc[:, "location"]:
    if i == "Afghanistan":
        boolean_list.append(True)
    else:
        boolean_list.append(False)
covid_data.loc[boolean_list, "total_cases"]
print(covid_data.loc[boolean_list, "total_cases"])
"""
0       0
1       0
2       0
3       0
4       0
     ... 
77     75
78     91
79    106
80    114
81    141
Name: total_cases, Length: 82, dtype: int64
"""
print(covid_data.loc[0:81, "total_cases"])  # Check
print(covid_data.loc[covid_data.location == "Afghanistan", "total_cases"])
# get help from https://blog.csdn.net/weixin_48964486/article/details/123152309
new_data = covid_data.loc[covid_data.date == "2020-03-31", :]
print("new_cases", np.mean(new_data.loc[:, "new_cases"]), np.std(new_data.loc[:, "new_cases"]))
print("new_deaths", np.mean(new_data.loc[:, "new_deaths"]), np.std(new_data.loc[:, "new_deaths"]))
"""
new_cases 640.4615384615385 4757.223283226196
new_deaths 37.92820512820513 281.08824232561113
"""
# The first one is mean and the second one is the standard deviation
print('{:.2%}'.format((np.sum(new_data.loc[:, "new_cases"]))/np.sum(new_data.loc[:, "total_cases"])))
"""
8.03%
"""
# get help from https://blog.csdn.net/u013553529/article/details/78567696#%E8%AF%B4%E6%98%8E
plt.boxplot([new_data.loc[:, "new_cases"], new_data.loc[:, "new_deaths"]])
plt.xticks(ticks=[1, 2], labels=["New Cases", "New Deaths"])
plt.ylabel("Number of Cases")
plt.title("New Cases and New Deaths on 31 March 2020")
plt.show()

