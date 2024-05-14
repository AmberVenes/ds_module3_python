# Import csv module
import csv

# Define variables
months = 0
total = 0

previous_value = 0
changes = []
months_difference = []

# Define path by copying the relative path of CSV
csvpath = "Pybank_Venes/Resources_bank/budget_data.csv"

# Use with to open and finish the program
with open(csvpath) as csvfile:

     # CSV reader specifies delimiter and separates data to make readable
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        months += 1 

        total = total + int(row[1])
        print(row)
        if (months == 1):

            previous_value = int(row[1])
        else:
            change = int(row[1]) - previous_value
            changes.append(change)
            months_difference.append(row[0])
            previous_value = int(row[1])

# use monthss to represnt the number of changes
monthss = months - 1

average_change = sum(changes) / monthss

top_change = max(changes)
top_month_x = changes.index(top_change)
top_month = months_difference[top_month_x]

bot_change = min(changes)
bot_month_x = changes.index(bot_change)
bot_month = months_difference[bot_month_x]

output = f"""Financial Analysis
------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {top_month} (${top_change})
Greatest Decrease in Profits: {bot_month} (${bot_change})"""

print(output)

with(open("output_venes_budget.txt", 'w') as f):
        f.write(output)

