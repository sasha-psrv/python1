# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

df = pd.read_csv("D:\python1\california_housing_train\california_housing_train.csv")
print(df[df['population']==df['population'].min()]['households'].max())
