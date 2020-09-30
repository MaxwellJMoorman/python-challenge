# PyBank

# Load CSV and os
import csv

# Create Lists
total_months = []
total_profit = []
date = []
monthly_profit_change = []

# Open CSV
with open('budget_data.csv') as csvDataFile:
    csvreader = csv.reader(csvDataFile)
    csv_header = next(csvDataFile)

    # Assign data into lists
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
        # Find net profit
        net_profit = sum(total_profit)
        date.append(row[0])

        #Find difference in dates
        date_increase = total_profit.index(max(total_profit))
        date_decrease = total_profit.index(min(total_profit))
    
    for rows in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[rows+1]-total_profit[rows])
    
        # Print results
        print('Financial Analysis')
        print('---------------------')
        print('Total Months: {}'.format(len(total_months)))
        print('Net Profit ${}'.format(net_profit))
        print('Greatest Increase in Profits (${}) {}'.format(max(monthly_profit_change),(date[date_increase])))
        print('Greatest decrease in Profits (${}) {}'.format(min(monthly_profit_change),(date[date_decrease])))
    


    

    


