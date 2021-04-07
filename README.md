# Python-Challenge

The Python challenge includes 2 projects, (1) PyBank - Analysis of Financial Data and (2) PyPoll - Analysis of Election Results. The primary function of the python scripts for both is to read CSV files, analyse the data and print the output on the terminal and on to a text file.

* For the challenge, the following CSV files were acquired from GitLab;
    * `budget_data.csv` of PyBank project
    * `election_data.csv` for PyPoll project
    These file are placed in the `Resources` folder of the respective project task.

* The results of the project are in the following files;
    * `pyBank_analysis.txt` is the output for PyBank project
    * `pyPoll_analysis.txt` is the output for PyPoll project
    These file are placed in the `Analysis` folder of the respective project task.

### PyBank Project
The task was to create a python script that analyzes financial records from the CSV file `budget_data.csv` file to calculate each of the following:

* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The average of the changes in "Profit/Losses" over the entire period
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period

**Note:**
The `Statistics` module was imported to utilize the `Average` function to compute the average of the changes in the Profit\Losses over the entire period.

### PyPoll Project
The task was to create a python script that analyzes election results from the CSV file `election_data.csv` file to calculate each of the following:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.