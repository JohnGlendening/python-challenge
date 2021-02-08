import csv

votes = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []

file_path = "./Resources/election_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

        print(row)

print("Election Results")
print("----------------------------------")
print(f"total:_votes {total_months}")


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
