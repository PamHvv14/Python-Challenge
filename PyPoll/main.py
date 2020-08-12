import os
import csv

budget_csv = os.path.join('..','PyPoll','Resources','election_data.csv')
with open(budget_csv,'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvfile)
    print("CSV Header: " + str(csv_header))

    rowcount = []
    candidates = set()

    for row in csvreader:
        rowcount.append(row[0])
        candidates.add(row[2]) 
    
    print(candidates)

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(len(rowcount)))
    print("----------------------------")
   
    print("----------------------------")

    print("----------------------------")