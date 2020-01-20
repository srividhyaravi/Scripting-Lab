import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")

print("heade descriptio")
print(df.head(5))

print("data descrption")
print(df.describe())

print(df[['Class',' Petal_Width']].groupby(['Class'],as_index=True).mean())

ax=sns.countplot(x=' Sepal_Width', data=df, palette="Set1",hue="Class")
ax.set(title="sepal width vs class",xlabel="width",ylabel="total")
plt.show()