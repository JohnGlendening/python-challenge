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

# Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


# open the csv file
with open(file_path) as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Loop through to find total months
    for row in csvreader:

        # Count the total of months
        total_months += 1

        # Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Calculate the average change in revenue between months over the entire period
        revenue_change = float(row["Profit/Losses"]) - previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]

        # The greatest increase in revenue (date and amount) over the entire period
        if revenue_change > greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row['Date']

        # The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row['Date']
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

    print("Financial Analysis\n")
    print("---------------------\n")
    print("Total Months: %d\n" % total_months)
    print("Total Revenue: $%d\n" % total_revenue)
    print("Average Revenue Change $%d\n" % revenue_average)
    print("Greatest Increase in Revenue: %s ($%s)\n" %
          (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n" %
          (greatest_decrease[0], greatest_decrease[1]))

# write changes to csv
with open(out_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % revenue_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" %
               (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" %
               (greatest_decrease[0], greatest_decrease[1]))
# results should look like
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
