#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Dependencies
import os
import csv


# In[2]:


#establish path
budget_data = os.path.join('budget_data.csv')


# In[3]:


#create lists and variables to be used
date = []
profit = []
monthly_changes = []
revenue_change_list = []
months = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
revenue_change = 0
previous_revenue = 0


# In[4]:


#open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #calculate total months
        months = months + 1
        #append date and profit lists to proper columns
        date.append(row[0])
     
        profit.append(row[1])
        #calculate total profit
        total_profit = total_profit + int(row[1])
        #calculate average change in profit month to month and make a list
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #calculate average change in profit
        average_change_profits = (total_change_profits/months)

        #calculate greatest increase and decrease in profit
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]             


# In[5]:


print("Financial Analysis")
print("-------------------------------------------------")
print("Total Months: " + str(months))
print("Total: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

     


# In[7]:


with open('financial_analysis.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("-----------------------------------------------------\n\n")
    text.write("    Total Months: " + str(months) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
  


# In[ ]:




