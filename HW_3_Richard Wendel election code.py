import csv
import os
    
csvpath = os.path.join("election_data.csv") 
pathout = os.path.join("Election Analysis.txt")
print(str(csvpath))
    
votes = 0
most_votes = -1
all_candidates = []
number_candidates = 0
candidate_choice = {}

# open csv, read csv
with open(csvpath) as poll_data:
    reader = csv.DictReader(poll_data)
    
    for row in reader:
        selected_candidate = row['Candidate']
        if selected_candidate not in all_candidates :
            number_candidates = number_candidates + 1
            all_candidates.append(selected_candidate)
            candidate_choice[selected_candidate] = 0
            
        candidate_choice[selected_candidate]=candidate_choice[selected_candidate]+1
        votes = votes + 1
        
        if candidate_choice[selected_candidate] > most_votes :
            most_votes = candidate_choice[selected_candidate]
            maxcandidate = selected_candidate


l1 = 'Election Data Breakdown'
l2 = '  -------------------------'
l3 = ('  Total Votes: %d' %(votes))
l4 = '  -------------------------'

output = l1 + '\n' + l2 + '\n' + l3 + '\n' + l4

for name in all_candidates :
    linex = ('  %s: %.3f%% (%d)' %(name,  100*candidate_choice[name]/(0.0+votes), candidate_choice[name]))
    output = output + '\n' + linex

print("--------------------------")
output = output + '\n' + ('  Winner: %s' %maxcandidate)
print("---------------------------")

print(output)


