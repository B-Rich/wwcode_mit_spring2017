# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:08:36 2017

@author: Марианна
"""

annual_salary=float(input("Enter the starting salary: "))
total_cost=1000000
semi_annual_raise=0.07
portion_down_payment = 0.25
monthly_salary=annual_salary/12
down_payment=0.25*total_cost
current_savings=0
n_months=0
r=0.04 #annual return
epsilon=100
low=0
#low=((down_payment/36)/monthly_salary)*10000
print(low)
high=10000
portion_s=(low+high)/2
print (portion_s)
num_guesses=0
while abs(current_savings-down_payment)>=epsilon and current_savings<down_payment:
    for i in range(36):
        monthly_savings=monthly_salary*(portion_s/10000)
        a=current_savings*(r/12)
        current_savings=current_savings+a+monthly_savings
        i+=1
        if i%6==0:
            monthly_salary=monthly_salary*(1+semi_annual_raise)
    if current_savings<down_payment:
        low=portion_s
    else:
        high=portion_s
    portion_s=round(high+low)/2
    num_guesses += 1
   

print("Best savings rate: ", portion_s/10000)
print("Steps in bisection search: ", num_guesses)
