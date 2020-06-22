# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status=data.Loan_Status.value_counts()

#Plotting bar plot


# bar chart
loan_status.plot(kind='bar')

# display plot
plt.show()

print(data.iloc[53,9])
# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False)
# Label X-axes and Y-axes
#Changing the x-axis label
plt.xlabel('Property Area')
#Changing the y-axis label
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()
print(property_and_loan['N'][1])
#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=True)

#Changing the x-axis label

plt.xlabel('Education Status')
#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()
print(education_and_loan['N'][1])
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')
plt.legend()

# Step 5
#Setting up the subplots

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3,ncols=1)

#Plotting scatter plot
ax_1.scatter(data['LoanAmount'],data['ApplicantIncome'])

ax_1.set_title('Applicant Income')

#Setting the subplot axis title
ax_2.scatter( data['LoanAmount'],data['CoapplicantIncome'])

ax_2.set_title('Coapplicant Income')

#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']


#Plotting scatter plot
ax_3.scatter(data['LoanAmount'],data['TotalIncome'])
ax_3.set_title('Total Income')


#Setting the subplot axis title



