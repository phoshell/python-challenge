import csv

csvpath = 'budget_data.csv'

# Initialize Variables with Values
total_months = 0
greatest_list = ["", 0]
decrease_list = []
grt_increase = 0
increase_date = ()
decrease_date = ()
grt_decrease = 0 
current_value = 0
row_count = 0
net_total = 0
sum_of_changes = 0
list_of_pnls = []
changes = []
dates =[]

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Profits and Losses
    # Add how manys months there are in the dataset
    for r in csvreader:
        pnl = int(r[1])                 # value from profit column
        list_of_pnls.append(pnl)        # profit loss list
        dates.append(r[0])              # list of dates cooresponding to profit 'n losses

        row_count = row_count + 1       # of rows = number of months
        net_total = net_total + pnl     # total of values from profit column
        
# Calculate diffs in the list of PNLs
# how many items are in this list?
for i in range(row_count - 1):
    this_pnl = list_of_pnls[i]
    next_pnl = list_of_pnls[i + 1]
    #print(list_of_pnls[i])
    changes.append(abs(next_pnl - this_pnl))

# i counts thru the list and looking for the cooresponding dates
for i in range(row_count):
    if list_of_pnls[i] > grt_increase:
        grt_increase = list_of_pnls[i]
        increase_date = dates[i]
    elif list_of_pnls[i] < grt_decrease:
        grt_decrease = list_of_pnls[i]
        decrease_date = dates[i] 

# AVERAGE CHANGES
for c in changes:
    sum_of_changes = sum_of_changes + c 

average_change = round(sum_of_changes / len(changes))

# GREATEST CHANGE
for current_value in list_of_pnls:
    if current_value > grt_increase:
        grt_increase = current_value 


#range(list_of_pnls + row_count /  
# loop starts here 
    # make a loop over the changes list, sum values/tot num of items

    #     total_months = total_months + 1
    #     net_amount += int(row[1]) 
    #     values_list [0] = row [0] 
    #     value_list = int(row[1]) 


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} $({grt_increase})") 
print(f"Greatest Decrease in Profits: {decrease_date} $({grt_decrease})")