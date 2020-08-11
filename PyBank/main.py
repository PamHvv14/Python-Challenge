import os
import csv

budget_csv = os.path.join('..','PyBank','Resources','budget_data.csv')
with open(budget_csv,'r') as csvfile:
    
    #print(csvreader)
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print("CSV Header: " + str(csv_header))
    rowcount = []
    total = []
    diff = []

    #Create list of first and second column to later count and sum them
    for row in csvreader:
        rowcount.append(row[0])
        total.append(int(row[1]))

    #For for calculations once first two values are obtained
    for i in range(1, len(rowcount)):
        diff.append(float(total[i] - total[i-1]))
        av_change = sum(diff) / len(diff)
        maxincrease = max(diff)
        mindecrease = min(diff)
        maxincreasedate = str(rowcount[diff.index(maxincrease)])
        mindecreasedate = str(rowcount[diff.index(mindecrease)])

    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: " + str(len(rowcount)))
    print("Total: $" + str(sum(total)))
    print("Average Change: $" + str(av_change))  
    print("Greatest Increase in Profits: " + str(maxincreasedate) + " $" + str(maxincrease))
    print("Greatest Decrease in Profits: " + str(mindecreasedate) + " $" + str(mindecrease))