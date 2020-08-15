import os
import csv

budget_csv = os.path.join('..','PyPoll','Resources','election_data.csv')
with open(budget_csv,'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print("CSV Header: " + str(csv_header))
 
    count = 0
    votes = {}

    for row in csvreader:
        candidate = row[2]
        count += 1
        if candidate in votes.keys():
            votes[row[2]] += 1
        else:
            votes[row[2]] = 1

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(count))
    print("----------------------------")

    for candidate in votes:
        percent = round((float(votes[candidate]))/float(count) * 100,2)
        print(candidate + ": " + str(percent) + "% " + str(votes[candidate]))
        
    print("----------------------------")

    print("----------------------------") 