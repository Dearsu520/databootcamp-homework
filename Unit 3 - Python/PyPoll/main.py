import os
import csv

filepath = os.path.join("PyPoll","Resources","election_data.csv")

total_votes = 0
candidates = []
vote_counts = []

with open(filepath,"r",encoding='utf-8') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_counts.append(1)
        else: 
            vote_counts[candidates.index(row[2])] += 1 

percentage = []
max_votes = 0
for candidate_votes in vote_counts:
    each_percentage = "{:.3f}".format(float(candidate_votes/total_votes*100))
    percentage.append(each_percentage) 
    if candidate_votes > max_votes:
        max_votes = candidate_votes
winner = candidates[vote_counts.index(max_votes)]

summary_table = zip(candidates,percentage,vote_counts) 

outputpath = os.path.join("PyPoll","Analysis","analysis.txt")

with open(outputpath,"w") as output:
    output.write("Election Results\n")
    output.write("----------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("----------------------\n")
    for number in range(len(candidates)):
        output.write(f"{candidates[number]}: {percentage[number]}% ({vote_counts[number]})\n")
    output.write("----------------------\n")
    output.write (f"Winner: {winner}\n")
    output.write("----------------------\n")


print ("Election Results")
print ("----------------------")
print (f"Total Votes: {total_votes}")
print ("----------------------")
for number in range(len(candidates)):
    print (f"{candidates[number]}: {percentage[number]}% ({vote_counts[number]})")
print ("----------------------")
print (f"Winner: {winner}")
print ("----------------------")



