import csv
import os

election_csv = "PyPoll/Resources/election_data.csv"
folder = "PyPoll"
analysis_file = os.path.join(folder,"analysis.txt")

#Initialize variables
t_votes = 0
can_votes = {}

# Read the CSV file
with open(election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        voter_id, country, candidate = row

        # Total votes
        t_votes += 1

        # Votes per candidate
        if candidate in can_votes:
            can_votes[candidate] += 1
        else:
            can_votes[candidate] = 1

# The winner
winner =max(can_votes, key = can_votes.get)

# Print the results
print("Election Results\n")
print("------------------------------------------------\n")
print(f"Total Votes: {t_votes}\n")
print("------------------------------------------------\n")

# Percentage per candidate
for candidate, votes in can_votes.items():
    percentage = (votes / t_votes) * 100
    print(f"{candidate}: {percentage:.2f}% ({votes})\n")

print("------------------------------------------------\n")
print(f"Winner: {winner}\n")
print("------------------------------------------------\n")

# Create and update the .txt file
with open(analysis_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------------------------------------\n")
    txtfile.write(f"Total Votes: {t_votes}\n")
    txtfile.write("------------------------------------------------\n")

    # Percentage per candidate
    for candidate, votes in can_votes.items():
        percentage = (votes / t_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.2f}% ({votes})\n")

    txtfile.write("------------------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("------------------------------------------------\n")