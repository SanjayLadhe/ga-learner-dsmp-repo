# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path) 
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar')
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
plt.pie(alignment,autopct='%.1f%%',shadow=True)



# --------------
#Code starts here

#Subsetting the data with columns ['Strength', 'Combat']
sc_df = data[['Strength','Combat']].copy()

#Finding covariance between 'Strength' and 'Combat'
sc_covariance = sc_df.cov().iloc[0,1]

#Finding the standard deviation of 'Strength'
sc_strength = sc_df['Strength'].std()

#Finding the standard deviation of 'Combat'
sc_combat = sc_df['Combat'].std()

#Calculating the Pearson's correlation between 'Strength' and 'Combat'
sc_pearson = sc_covariance/(sc_combat*sc_strength)

print("Pearson's Correlation Coefficient between Strength and Combat : ", sc_pearson)


#Subsetting the data with columns ['Intelligence', 'Combat']
ic_df = data[['Intelligence','Combat']].copy()

#Finding covariance between 'Intelligence' and 'Combat'
ic_covariance = ic_df.cov().iloc[0,1]

#Finding the standard deviation of 'Intelligence'
ic_intelligence = ic_df['Intelligence'].std()

#Finding the standard deviation of 'Combat'
ic_combat = ic_df['Combat'].std()

#Calculating the Pearson's correlation between 'Intelligence' and 'Combat'
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)

#Code ends here


# --------------
#Code starts here

#Find the quantile=0.99 value of 'Total' column
total_high= data['Total'].quantile(q=0.99)

#Subsetting the dataframe based on 'total_high' 
super_best=data[data['Total']>total_high]

#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])

#Printing the names
print(super_best_names)

#Code ends here



# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3,figsize=[40,30])
ax_1.boxplot(super_best['Intelligence'])
ax_1.set(title='Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set(title='Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set(title='Power')
plt.show()


