import csv

vote_count = {}
percentage = {}
candidate = []

total_votes = 0

file_path = "./Resources/election_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)

    for row in csvreader:
        total_votes += 1
        if row[2] in candidate and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1
        # else create new spot in list for candidate
        else:
            candidate.append(row[2])
            vote_count[row[2]] = 1

# Percentage calculation
for key, value in vote_count.items():
    percentage[key] = str(round((value/total_votes)*100, 3)
                          ) + "% ("+str(value) + ")"

# winner
winner = max(vote_count.keys(), key=(lambda k: vote_count[k]))


print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------------")
print(f"Percentage: {percentage}")
print(f"Winner: {winner}")


# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
