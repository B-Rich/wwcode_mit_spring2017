# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:22:53 2017

@author: Marianna
"""

annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal(i.e. 0.1 for 10%): "))
total_cost=float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi­annual salary raise, as a decimal(i.e. 0.1 for 10%): "))
portion_down_payment = 0.25
monthly_salary = annual_salary/12
down_payment = 0.25*total_cost
current_savings = 0
n_months = 0
r = 0.04

while current_savings <= down_payment:
    monthly_savings = monthly_salary*portion_saved
    a = current_savings*(r/12)
    current_savings = current_savings + a + monthly_savings
    n_months += 1
    if n_months % 6 == 0:
       monthly_salary += monthly_salary*semi_annual_raise   
print("Number of months: ", n_months)

