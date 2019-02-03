import csv

csvpath = 'election_data.csv'

total_votes = 0
candidate_dict = {}
candidate_list = []
percent_vote = []
# For instance, key: "row[2], or candidate name", value: "number of votes"

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # FINDING ALL CANDIDATES & COUNTING VOTES:
    for row in csvreader:
        total_votes = total_votes + 1
        # Populate list with candidates  
        if row[2] not in candidate_dict.keys():
            candidate_dict[row[2]] = 1 
        else:
            candidate_dict[row[2]] += 1
    for each in candidate_dict.keys():
         print(candidate_dict[each])


candidate_list = list(candidate_dict.keys())

# print(candidate_list)
# This counter keeps track of how many candidates we have
can_counter = len(candidate_list)
winner = ""
win_value = 0

for i in range(can_counter):
    candidate = candidate_list[i] 
    if candidate_dict[candidate] > win_value:
        win_value = candidate_dict[candidate]
        winner = candidate
        
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")

# pThis for loop will calcuate percentage of total votes per candidate
for i in range(can_counter):
    candidate = candidate_list[i] 
    percent_vote = candidate_dict[candidate] / total_votes * 100
    print(f"{candidate_list[i]}: {round(percent_vote, 3)}% ({candidate_dict[candidate]})")

print(f'''-------------------------
-------------------------
Winner: {winner} with {win_value} votes
------------------------- ''')
