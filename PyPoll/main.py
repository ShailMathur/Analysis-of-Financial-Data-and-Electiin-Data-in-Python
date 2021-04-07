import csv
import os

# define relative path for the input and output files
path = "/Users/vrmathur/Documents/Gtech/Python-Challenge/PyPoll/"
inputfile = os.path.join(path, "Resources", "election_data.csv")
outputfile = os.path.join(path, "Analysis", "pyPoll_analysis.txt")

# read the CSV file and store values of each column into lists
with open(inputfile) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile, delimiter=',')

    # create empty lists and variables for storing values and calculations from data
    Candidate = []
    VoteCounts = []
    VotePercent = []
    TotalVotes = 0
    WinnerCount = 0

    # store header rows into a Headers list
    Headers = next(csvreader)

    for column in csvreader:
       VoteCounts.append(column[0])
       Candidate.append(column[2])

Total_Votes = (len(VoteCounts))

# count each number of candidates in the candidates list
khan_total = Candidate.count('Khan')
correy_total = Candidate.count('Correy')
li_total = Candidate.count('Li')
o_tooley_total = Candidate.count("O'Tooley")


# calculate percentage of votes for each candidate 
khan_percent = khan_total / Total_Votes
correy_percent = int(correy_total) / int(Total_Votes)
li_percent = li_total / Total_Votes
o_tooley_percent = o_tooley_total / Total_Votes


# compare Votes and pick winner with the most votes
if khan_total > correy_total > li_total > o_tooley_total:
       Winner = "Khan"
elif correy_total > khan_total > li_total > o_tooley_total:
       Winner = "Correy"
elif li_total > khan_total > correy_total > o_tooley_total:
       Winner = "Li"
elif o_tooley_total > khan_total > correy_total > li_total:
       Winner = "O'Tooley_total"

# print each candidate's name, vote percentage, and total number of votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {Total_Votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {Winner}')
print(f'-------------------------')









