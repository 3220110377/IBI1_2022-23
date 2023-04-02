import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/ibi/IBI1_2022-23/Practical7")  # Change the working directory
print(os.getcwd())  # Show the working directory
print(os.listdir())  # List the file under the directory
covid_data = pd.read_csv("full_data.csv")
print(covid_data.head(5))
print(covid_data.info())
print(covid_data.describe())
print(covid_data.iloc[2, 0:5])
print(covid_data.iloc[0:2, :])
print(covid_data.iloc[0:10:2, 0:5])
