import os
import csv

budget_csv = os.path.join('..','PyPoll','Resources','election_data.csv')
with open(budget_csv,'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print("CSV Header: " + str(csv_header))

    rowcount = []
    candidates = []
    votes = {}

    for row in csvreader:
        rowcount.append(row[0])
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] in votes.keys():
            votes[row[2]] += 1
        else:
            votes[row[2]] = 1

    print(candidates)
    print(votes)

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(len(rowcount)))
    print("----------------------------")
   
    print("----------------------------")

    print("----------------------------")