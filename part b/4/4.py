import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

td=pd.read_csv("train.csv")

print("data description")
print(td.head(5))

print("--header descrption--")
print(td.describe())

td.drop(['Ticket','Fare'],axis=1,inplace=True)
print(td.head(5))

td["Embarked"]=td["Embarked"].fillna('S')
td["Survived"]=td["Survived"].map({0:"death",1:"survive"})

ax=sns.countplot(data=td,x="Survived",hue="Pclass",palette="Set1")
ax.set(title="class vs survival",xlabel="survival",ylabel="class")
plt.show()
