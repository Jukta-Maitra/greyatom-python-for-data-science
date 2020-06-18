# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census=np.concatenate((new_record,data))


age=np.array(census[:,:1])
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
min_race=0
min_race=min(len_0,len_1,len_2,len_3,len_4)
if min_race==len_0:
    minority_race=0
if min_race==len_1:
    minority_race=1
if min_race==len_2:
    minority_race=2
if min_race==len_3:
    minority_race=3
if min_race==len_4:
    minority_race=4

print(minority_race)

senior_citizens=census[census[:,0]>60]
working_hours_sum=sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(round(avg_pay_high,2))
print(round(avg_pay_low,2))

np.array_equal(avg_pay_high,avg_pay_low)



