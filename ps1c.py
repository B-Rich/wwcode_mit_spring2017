# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:08:36 2017

@author: Marianna
"""

annual_salary=float(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = 0.25*total_cost
current_savings = 0
r = 0.04 #annual return
epsilon = 100 # +- $100 from total cost
low = 0
high = 10000
num_guesses = 0

while abs(down_payment - current_savings) > epsilon:
    current_savings = 0
    monthly_salary = annual_salary/12
    portion_s = int((high+low)/2)
    for i in range (36):
        if i != 0 and i % 6 == 0:
            monthly_salary += monthly_salary*semi_annual_raise
        #print(monthly_salary)
        monthly_savings = monthly_salary*(portion_s/10000)
        a = current_savings*(r/12)
        current_savings += a + monthly_savings
            
    if current_savings - down_payment < 0:
        low = portion_s
    else:
        high = portion_s
    num_guesses += 1 
    
    if low > 9900:
        print("It is not possible to pay the down payment in three years.")
        break

print("Best savings rate: ", portion_s/10000)
print("Steps in bisection search: ", num_guesses)
    

