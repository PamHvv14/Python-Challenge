import os
import csv

budget_csv = os.path.join('..','PyPoll','Resources','election_data.csv')
with open(budget_csv,'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvfile)
    print("CSV Header: " + str(csv_header))

    rowcount = []
    candidates = []
    votes = [0,0,0,0]

    for row in csvreader:
        rowcount.append(row[0])
        if row[2] not in candidates:
            candidates.append(row[2])

    for i in range(len(candidates)+1):
        for row in csvreader:
            if row[2] == candidates[i-1]:
                votes[i-1] = votes[i-1] +1

    print(candidates)
    print(votes)

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(len(rowcount)))
    print("----------------------------")
   
    print("----------------------------")

    print("----------------------------")