import os
import csv

budget_csv = os.path.join('..','PyBank','Resources','budget_data.csv')

with open(budget_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print("CSV Header: " + str(csv_header))

    rowcount = sum(1 for row in csvreader)
    print("Total Months: " + str(rowcount))

    #value = [csvreader[1]]
    #listA = [
    11,
    18,
    19,
    21,
    46
]

#print(sum(listA))