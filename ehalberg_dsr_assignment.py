# DSR Base Assignment Palindrome Data
# Applicant: Ernest Halberg
# 17-05-2021

import pandas as pd

hiv_df = pd.read_excel('~/Downloads/pone.0212445.s004.xlsx', skiprows=1)

############################################################################################################

#Note initial data exploration was done eyeballing in excel as I noticed it is a small dataset.

#Checked for missing values - none

#Inspected columns to understand what is represented in the dataset

#Inspected datatype and ranges (also did a hiv_df.describe() in jupyter for further inspection, excluded here)

#Skipped initial caption upon reading into python

#Solutions are based on knowledge of how clean the data is and assumes consistency

############################################################################################################

# a) What is the total number of people living with HIV (NoPLHIV) in the listed districts according to the Survey estimate?

hiv_df[hiv_df['Estimate']=='Survey']['NoPLHIV'].sum()

#6409903

############################################################################################################

# b) What is the average NoPLHIV of the two estimates used for “Xhariep”?

hiv_df[hiv_df['District']=='Xhariep']['NoPLHIV'].mean()

#12247.5

############################################################################################################

# c) Add a column and populate it with the number of people not living with HIV for each row.

#Rounded result and casted to int since we are looking at estimates of people.

hiv_df['not_living_with_hiv'] = round(hiv_df['NoPLHIV']/(hiv_df['Prevalence_%']/100) - hiv_df['NoPLHIV']).astype(int)

############################################################################################################

# d) What is the total NoPLHIV in all the cities (districts with the word “city” or “metro” in the name)? 

hiv_df[hiv_df['District'].str.contains('Metro')]['NoPLHIV'].sum() + hiv_df[hiv_df['District'].str.contains('City')]['NoPLHIV'].sum() 

#2572733

#Used pandas' built-in regex due to the clean nature of the data. 
#Upon inspection there were no lower case values for 'City' and 'Metro' so this was a safe option

# 3) Write the original data (without the caption - originally row 1) with the extra columns as comma-separated values (CSV) to a new .csv file.

hiv_df.to_csv('~/Downloads/hiv_df.csv', index=False)

############################################################################################################

# Time to complete ~30 minutes, about 20 minutes spent double checking for trick questions and triple checking outputs

############################################################################################################
