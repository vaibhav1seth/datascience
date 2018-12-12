import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

bf_df = pd.read_csv('BlackFriday.csv')

print('********Data Headers*******')
print(bf_df.head())
print(bf_df.info())
print(bf_df.describe())


print("\n\n*******Data headers before dropping columns*******\n")
print(bf_df.head(5))

print("\n\n*******Data Manipulation*******\n")
bf_df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'],axis=1,inplace=True)
print("\n\n********Data after dropping unnecessary columns******\n")
print(bf_df.head(5))

bf_df["City_Category"]=bf_df["City_Category"].fillna("D")


bf_df['City_Category']=bf_df['City_Category'].map({
	"A":"Metro Cities",
	"B":"Small Towns",
	"C":"Villages",
	"D":"Not Applicable"
})

print("\n\n*******Data values after changing City Category Values*******\n")
print(bf_df['City_Category'].head(5))

bf_df['Marital_Status']=bf_df['Marital_Status'].map({
	1:"Married",
	0:"UnMarried"
})

print("\n\n*******Data values after changing Marital status Values*******\n")
print(bf_df['Marital_Status'].head(5))
print("\n\n\n**** DATA VISUALIZATIONS****\n\n")

print("Visualization #1 :Tally of the Number of male and female based on baseball caps and wine tumbler") 
ax=sns.countplot(x='Product_Category_1',hue='Gender',palette='Set1',data=bf_df)
ax.set(xlabel='No. of baseball caps',ylabel='Number of people having x number of baseball caps',title='tally of products category 1')
plt.show()


 
ax=sns.countplot(x='Product_Category_2',hue='Gender',palette='Set1',data=bf_df)
ax.set(xlabel='No. of Wine Tumblers',ylabel='Number of people having x number of Wine Tumblers',title='tally of products category 2')
plt.show()

print("Visualization #2 :Total number of male and female belonging to each category")

ax= sns.countplot(x='City_Category',hue='Gender',palette='Set2',data=bf_df)
ax.set(xlabel="City Category",ylabel="Total",title="No.of persons in each category")
plt.show()




