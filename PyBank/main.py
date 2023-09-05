import csv
import os

budget_csv = "PyBank/Resources/budget_data.csv"
folder = "PyBank"
analysis_file =os.path.join(folder,"analysis.txt")

# Initialize variables
t_months = 0
net_total = 0

changes = []

greatest_inc = {"date": "", "amount": 0}
greatest_dec = {"date": "", "amount": 0}

# Read the cvs file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    previous_profit_loss = None

    for row in csvreader:
        date,profit_loss = row
        profit_loss = int(profit_loss)

        # Total number of months
        t_months += 1

        # Net total 
        net_total += profit_loss

        # Change in Profit/Losses
        if previous_profit_loss is not None:
            change = profit_loss - int(previous_profit_loss)
            changes.append(change)

            # Greatest increase and decrease
            if change > greatest_inc["amount"]:
                greatest_inc = {"date": date, "amount": change}
            elif change < greatest_dec["amount"]:
                greatest_dec = {"date": date, "amount": change}

        previous_profit_loss = profit_loss

average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {t_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc['date']} (${greatest_inc['amount']})")
print(f"Greatest Decrease in Profits: {greatest_dec['date']} (${greatest_dec['amount']})")
print("------------------------------------------------")

# Create and update the .txt file
with open(analysis_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------------------\n")
    txtfile.write(f"Total Months: {t_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_inc['date']} (${greatest_inc['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_dec['date']} (${greatest_dec['amount']})\n")
    txtfile.write("------------------------------------------------\n")