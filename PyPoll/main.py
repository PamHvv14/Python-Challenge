import os
import csv

budget_csv = os.path.join('..','PyPoll','Resources','election_data.csv')

with open(budget_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print("CSV Header: " + str(csv_header))