import csv
import os
import statistics as st #to calculate average

# --- define relative path for the input and output files -
inputfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Analysis", "pyBank_analysis.txt")

# --- read the CSV file and store values of each column into lists ---
with open(inputfile) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # --- create empty lists for storing values and calculations from data ---
    Dates = []
    ProLoss = []
    ProLossChanges = []

    # --- store header rows into a Headers list ---
    Headers = next(csvreader)

    # --- for loop to go through each row in the CSV file and append values from date column to the 'Dates' list and Profits/Losses column to the 'ProfLoss' list ---
    for row in csvreader:
        Dates.append(row[0])
        ProLoss.append(int(row[1]))

print(Headers)
print(ProLoss)

# --- for loop to go through each value in Profits/Losses list and calculate total ---
totalProLoss = 0
for i in ProLoss:
    totalProLoss = i + totalProLoss

print("Total Profit\Loss = $" + str(totalProLoss))

