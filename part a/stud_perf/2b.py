import numpy as np,seaborn as sns,pandas as pd
import matplotlib.pyplot as plt

stud=pd.read_csv("StudentsPerformance.csv")
print("data description")
print(stud.describe())
print("----head description---")
print(stud.head(5))

print("--after dropping---")
stud.drop(['lunch'],axis=1,inplace=True)
print(stud.head(5))

stud["parental level of education"]=stud["parental level of education"].fillna("not applicable")
print(stud["parental level of education"])

ax=sns.countplot(data=stud,palette="Set1",hue="gender",x="test preparation course")
ax.set(title="sex vs test prepartion",xlabel="test preparartion",ylabel="sex")
plt.show()