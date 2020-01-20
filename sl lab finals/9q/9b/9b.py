import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bf=pd.read_csv("BlackFriday.csv")

print("data description")
print(bf.describe())

print("header description")
print(bf.head(5))

bf["City_Category"]=bf["City_Category"].fillna('A')
print(bf["City_Category"])

bf["City_Category"]=bf["City_Category"].map({"A":"metrocities","B":"smalltowns","C":"villages"})
print(bf["City_Category"])

ax=sns.countplot(data=bf,x="Gender",hue="City_Category",palette="Set1")
ax.set(title="sex vs city_category",xlabel="gender",ylabel="total")
plt.show()