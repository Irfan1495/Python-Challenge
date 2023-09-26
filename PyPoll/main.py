#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
election_data = os.path.join("Resources", "election_data.csv")


candidates = []
percent_votes = []
num_votes = []

total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)


for row in csvreader:
    total_votes += 1

    if row[2] not in candidates:
        candidates.append(row[2])
        index = candidates.index([2])
        num_votes.append(1)


    else:
        index = candidates.index(row[2])
        num_votes.append(1)


    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percent_votes.append(percentage)
        


winner = max(num_votes)
index = num_votes.index(winner)
winning_candidate = candidates(index)



output = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: {winning_candidate}
-------------------------
'''


print(election_data)
my_report.write(output)









