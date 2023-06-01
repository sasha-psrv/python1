# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

import pandas as pd

df = pd.read_csv("D:\python1\california_housing_train\california_housing_train.csv")

print(df.median_house_value.max() , df.median_house_value.min() )

print(df.loc[(df.median_income == 3.1250), ['median_house_value']].max())

# print(df.loc[(df.median_house_value.min()), ['population']].max())

df1 = df.loc[df.median_house_value < df.median_house_value.quantile(.15)]
print(df1.population.max())
print(df1)
print( df.median_house_value.quantile(.25))