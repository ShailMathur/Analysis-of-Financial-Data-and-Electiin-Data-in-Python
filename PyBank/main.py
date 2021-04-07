import csv
import os
import statistics as st #to calculate average

# define function to calculate average of the list
def Average(list):

    # round the number to 2 decimal points and return value
    return round(st.mean(list), 2) 

# define relative path for the input and output files-
#path = "/Users/vrmathur/Documents/Gtech/Python-Challenge/PyBank/"
inputfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Analysis", "pyBank_analysis.txt")

# read the CSV file and store values of each column into lists
with open(inputfile) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # create empty lists for storing values and calculations from data
    Dates = []
    ProLoss = []
    ProLossChanges = []

    # store header rows into a Headers list
    Headers = next(csvreader)

    # for loop to go through each row in the CSV file and append values from date column to the 'Dates' list and Profits/Losses column to the 'ProfLoss' list
    for row in csvreader:
        Dates.append(row[0])
        ProLoss.append(int(row[1]))

# for loop to go through each value in Profits/Losses list and calculate total
totalProLoss = 0
for i in ProLoss:
    totalProLoss = i + totalProLoss


# use list comprehension to create a new list with difference values of each successive row (next row - current row)
ProLossChanges = [ProLoss[i+1] - ProLoss[i] for i in range(0,len(ProLoss)-1)]


# calculate average change by calling the function and store in variable
AverageChange = Average(ProLossChanges)


# insert a value of zero at index 0 of the ProLossChanges list as there is no previous data to subtract for the first month (thus also making the list equal in length to Dates and ProLoss lists for index finding later)
ProLossChanges.insert(0,0)


# find the max and min change in profits and the corresponding dates these changes were obeserved
greatest_increase_profits = max(ProLossChanges)

increase_date = Dates[ProLossChanges.index(greatest_increase_profits)]

greatest_decrease_profits = min(ProLossChanges)

decrease_date = Dates[ProLossChanges.index(greatest_decrease_profits)]


# generating output
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {len(Dates)}')
print(f'Total: ${totalProLoss}')
print(f'Average Change: ${AverageChange}')
print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})')
print(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits})')


with open(outputfile, 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'___________________________', file=text_file)
    print(f'Total Months: {Dates}', file=text_file)
    print(f'Total: ${totalProLoss}', file=text_file)
    print(f'Average Change: ${AverageChange:.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {increase_date} ({greatest_increase_profits})', file=text_file)
    print(f'Greatest Decrease in Profits: {decrease_date} ({greatest_decrease_profits})', file=text_file)