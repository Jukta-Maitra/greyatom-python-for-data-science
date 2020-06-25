# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
#Code starts here
categorical_var=bank_data.select_dtypes(include = 'object')

numerical_var=bank_data.select_dtypes(include = 'number')

print(categorical_var.shape)
print(numerical_var.shape)

banks=bank_data.drop(columns='Loan_ID')

print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
banks.fillna(bank_mode,inplace=True)
print(banks.shape)

avg_loan_amount=banks.pivot_table(values=['LoanAmount'],index=['Gender','Married','Self_Employed'],aggfunc=np.mean)

print(avg_loan_amount['LoanAmount'][1],2)

loan_approved_se=banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()
loan_approved_nse=banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()
percentage_se=loan_approved_se*100/614
print(percentage_se)
percentage_nse=loan_approved_nse*100/614
print(percentage_nse)


loan_term=banks['Loan_Amount_Term'].apply(lambda x:int(x)/12)

big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

loan_groupby=banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby['ApplicantIncome','Credit_History']

mean_values=loan_groupby.agg([np.mean])
print(mean_values.iloc[1,0],2)
print(mean_values)












