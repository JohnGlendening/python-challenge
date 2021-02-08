import csv
# The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
total_profit_loss_amount = 0
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
average_profit_loss = 0.00
# The greatest increase in profits(date and amount) over the entire period
greatest_increase = {"date": "", "amount": 0}
# The greatest decrease in losses(date and amount) over the entire period
greatest_decrease = {"date": "", "amount": 0}

file_path = "./Resources/budget_data.csv"
out_file = "./Analysis/output.txt"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
     # The total number of months included in the dataset
        total_months = total_months + 1
        date = row[0]
        total = float(row[1])
        profit = float(row[1])
        initial_profit = 0
    # The net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        total_profit_loss_amount += current_month_profit_loss
    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

    # The greatest increase in profits(date and amount) over the entire period
        if (profit > greatest_increase["amount"]):
            greatest_increase["date"] = date
            greatest_increase["amount"] = profit
    # The greatest decrease in losses(date and amount) over the entire period
        if (profit < greatest_decrease["amount"]):
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = profit

print("financial Analysis")
print("----------------------------------")
print(f"total_months: {total_months}")
print(f"Total: {total_profit_loss_amount}")
print(f"Average Change: {average_profit_loss}")
print(
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# write to a file
with open(out_file, 'w') as outputFile:
    outputFile.write("financial Analysis\n"),
    outputFile.write("----------------------------------\n")
    outputFile.write(f"total_months: {total_months}\n")
    outputFile.write(f"Total: ${total_profit_loss_amount}\n")
    outputFile.write(f"Average  Change: ${average_profit_loss}\n")
    outputFile.write(
        f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"),
    outputFile.write(
        f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# results should look like
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
