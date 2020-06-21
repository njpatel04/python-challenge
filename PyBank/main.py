import csv
import os

budget_csv = os.path.join('..', 'Resources', 'PyBank_Resources_budget_data.csv')

count = 0
Max = 0
Min = 0
total = 0
Avg = 0

monty_changes = []
Month_list = []
budget_list = []

# Reading CSV file / creating Budget & Month lists / caculating Total & Total months
with open(budget_csv) as budgetfile:

    budgetreader = csv.reader(budgetfile, delimiter=',')

    budgetheader = next(budgetreader)  # Header line from csv file

    for row in budgetreader:
    
        count = count + 1  # counting months by couting number of list
        total = total + int(row[1])

        Month_list.append(row[0])
        budget_list.append(row[1])

# Calculating Greatest Increase in profits
for i in range(len(budget_list)):
    if int(budget_list[i]) - int(budget_list[i-1]) > Max:
        Max = int(budget_list[i]) - int(budget_list[i-1])
        Max_Month = Month_list[i]

# Calculating Greatest Decrease in profits
for i in range(len(budget_list)):
    if int(budget_list[i]) - int(budget_list[i-1]) < Min:
        Min = int(budget_list[i]) - int(budget_list[i-1])
        Min_Month = Month_list[i]

# Calculating Average Change
Avg = int(budget_list[count-1]) - int(budget_list[0])
Avg = round(float(Avg / (count-1)), 2)


print("Financial Analysis")
print("-----------------------------------------------------------")
print(f'Total Months: {count}')
print(f'Total: ${total}')
print(f'Average Change: ${Avg}')
print(f'Greatest Increase in Profits: {Max_Month} (${str(Max)})')
print(f'Greatest Decrease in Profits: {Min_Month} (${str(Min)})')


Output_text = os.path.join('..', 'PyBank_Output.txt')

with open(Output_text, 'w') as textfile:

    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------------------------------------\n")
    textfile.write(f'Total Months: {count}\n')
    textfile.write(f'Total: ${total}\n')
    textfile.write(f'Average Change: ${Avg}\n')
    textfile.write(f'Greatest Increase in Profits: {Max_Month} (${str(Max)})\n')
    textfile.write(f'Greatest Decrease in Profits: {Min_Month} (${str(Min)})\n')
