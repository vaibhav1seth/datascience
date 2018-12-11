import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

perf_df=pd.read_csv('StudentsPerformance.csv')

print('====Data headers====')
perf_df.head()

perf_df.info()

perf_df.describe()

perf_df1 = perf_df.drop(['lunch', 'test preparation course'], axis=1)
perf_df1.head()

perf_df["parental level of education"] = perf_df["parental level of education"].fillna("Not applicable")
print(perf_df.head(5))

perf_df["race/ethnicity"]=perf_df["race/ethnicity"].map({
    "group A" : "Asian students",
    "group B" : "African students",
    "group C" : "Afro-Asian students",
    "group D" : "American students",
    "group E" : "European students"
})
print(perf_df.head(10))

ax = sns.countplot(x="test preparation course",hue='gender',palette='Set3',data=perf_df)
ax.set(title="Course completion based on gender", xlabel='Course', ylabel='Total')
plt.show()



ax = sns.countplot(x="race/ethnicity",hue="gender",palette="Set2",data=perf_df)
ax.set(title="Total number of male and female students belonging to each group", xlabel="Groups", ylabel="Total")
plt.show()

interval=(0,40,50,60,75)
categories = ["Fail", "2nd class","1st class","Distinction"]
perf_df["Marks_cats"]=pd.cut(perf_df.mathscore,interval,labels=categories)
ax=sns.countplot(x="Marks_cats",hue="gender",palette="Set1",data=perf_df)
ax.set(title="Marks categorisation for math",xlabel="Categories",ylabel="Number of students")
plt.show()

perf_df["Marks_Cats"]=pd.cut(perf_df.readingscore,interval,labels=categories)
ax=sns.countplot(x="Marks_Cats",hue="gender",palette="Set1",data=perf_df)
ax.set(title="Marks categorisation for reading",xlabel="Categories",ylabel="Number of students")
plt.show()

perf_df["Marks_Cats"]=pd.cut(perf_df.writingscore,interval,labels=categories)
ax=sns.countplot(x="Marks_Cats",hue="gender",palette="Set1",data=perf_df)
ax.set(title="Marks categorisation for writing",xlabel="Categories",ylabel="Number of students")
plt.show()
