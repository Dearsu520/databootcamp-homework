import os
import csv

filepath = os.path.join("PyBank","Resources","budget_data.csv")

total_months = 0
total_profit = 0
previous_profit = 0
current_change = 0
all_changes = []
total_changes = 0
max_change = 0
min_change = 0 

with open(filepath,"r",encoding='utf-8') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    
    for row in csvreader:
        total_months += 1
        total_profit = total_profit + int(row[1])
        current_change = int(row[1])-previous_profit
        total_changes = total_changes + current_change
        all_changes.append(current_change)
        if current_change > max_change:
            max_change = current_change
            max_date = row[0]
        if current_change < min_change:
            min_change = current_change   
            min_date = row[0]
        previous_profit = int(row[1])
    
    total_changes = total_changes - all_changes[0]
    all_changes.pop(0)
    average_change = round(float(total_changes/len(all_changes)),2)

output_result = ("Financial Analysis\n"
"----------------------------------\n"
f"Total Months: {total_months}\n"+f"Total: ${total_profit}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_date} (${max_change})\n"
f"Greatest Decrease in Profits: {min_date} (${min_change})\n")

outputpath = os.path.join("PyBank","Analysis","analysis.txt")

with open(outputpath,"w") as output:
    output.write(output_result)
   
print (output_result)
