import csv
import os

election_csv = os.path.join('..', 'Resources', 'PyPoll_Resources_election_data.csv')

count = 0

Candidate = []
Khan_list = []
Correy_list = []
Li_list = []
OTooley_list = []

# Reading CSV file / creating Budget & Month lists / caculating Total & Total months
with open(election_csv) as electionfile:

    electionreader = csv.reader(electionfile, delimiter=',')

    electionheader = next(electionreader)  # Header line from csv file

    for row in electionreader:
    
        count = count + 1  # counting rows in the CSV file
        if row[2] == "Khan":
            Khan_list.append(row[2])
        elif row[2] == "Correy":
            Correy_list.append(row[2])
        elif row[2] == "Li":
            Li_list.append(row[2])
        elif row[2] == "O'Tooley":
            OTooley_list.append(row[2])

Khan_vote = len(Khan_list)
Correy_vote = len(Correy_list)
Li_vote = len(Li_list)
OTooley_vote = len(OTooley_list)

Khan_Percent = round(( Khan_vote / count ) * 100 , 3)
Correy_Percent = round(( Correy_vote / count ) * 100 , 3)
Li_Percent = round(( Li_vote / count ) * 100 , 3)
OTooley_Percent = round(( OTooley_vote / count ) * 100 , 3)

percent = [Khan_Percent, Correy_Percent, Li_Percent, OTooley_Percent]
winnername = ["Khan", "Correy", "Li", "O'Tooley"]

winner = ''

for w in range(len(percent)):
    if percent[w] > percent[w-1]:
        winner = winnername[w]


print("Election Results")
print("-----------------------------------------------------------")
print(f'Total Votes: {count}')
print("-----------------------------------------------------------")
print(f'Khan: {Khan_Percent}% ({Khan_vote})')
print(f'Correy: {Correy_Percent}% ({Correy_vote})')
print(f'Li: {Li_Percent}% ({Li_vote})')
print(f"O'Tooley: {OTooley_Percent}% ({OTooley_vote})")
print("-----------------------------------------------------------")
print(f'Winner: {winner}')
print("-----------------------------------------------------------")

Output_text = os.path.join('..', 'PyPoll_Output.txt')

with open(Output_text, 'w') as textfile:

    textfile.write("Election Results\n")
    textfile.write("-----------------------------------------------------------\n")
    textfile.write(f'Total Votes: {count}\n')
    textfile.write("-----------------------------------------------------------\n")
    textfile.write(f'Khan: {Khan_Percent}% ({Khan_vote})\n')
    textfile.write(f'Correy: {Correy_Percent}% ({Correy_vote})\n')
    textfile.write(f'Li: {Li_Percent}% ({Li_vote})\n')
    textfile.write(f"O'Tooley: {OTooley_Percent}% ({OTooley_vote})\n")
    textfile.write("-----------------------------------------------------------\n")
    textfile.write(f'Winner: {winner}\n')
    textfile.write("-----------------------------------------------------------\n")

