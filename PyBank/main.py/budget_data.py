import os
import csv

budget_data_csv = os.path.join("." "Resources","budget_data.csv")

#budget_data.csv = 'Users\JMARS\OneDrive\Desktop\Bootcamp\HOMEWORK\python-challenge\python-challenge\PyBank\Resources\budget_data.csv'
print(budget_data_csv)

total_volume = 0
total_months = 0
previous_value = 0
total_changes = 0

greatest_increase = 0
greatest_decrease = 99999999

total_profit = 0
monthly_profit_change = 0

for row in reader:
        
        print(row)
        print(row[0])

        first_name = row[0]
        phone_number = row[2]

        total_months += 1
        total_profit +=float(row[1])

        current_value = float(row[1])
        change = current_value - previous_value

        if change > greatest_increase:
              greatest_increase = change
              greatest_increase_month = row[0]

        if change < greatest_decrease:
              greatest_decrease = change
              greatest_decrease_month = row[0]     

        previous_value = float(row[1])

        total_changes=+change

average_change = total_changes / total_months - 1

output_file = os.path.join(".","analysis","budget_report.txt")

output = (f"Financial Analysis\n"
    f".......\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_profit}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase})\n"
    f"Greatest Increase in Profits: {greatest_decrease_month} ({greatest_decrease})\n")
    
print(output)