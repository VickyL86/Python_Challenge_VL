# First we'll import the os module
# This will allow us to create file paths across operating systems
import csv
import os


# Module for reading CSV files
import pandas as pd

#found apporpriate module on ChatGPT
from collections import Counter

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Pull and read the file --> https://datatofish.com/import-csv-file-python-using-pandas/
df = pd.read_csv(r'C:\Users\lasot\OneDrive\Desktop\Data Bootcamp\Module 3 Python\PyPoll\Resources\election_data.csv')

#print my "header" info for the txt later one
print('Election Results')
print('--------------------------------------------------------------')
print('Total Votes:', len(df.index))
print('--------------------------------------------------------------')


#Pulling a list from the candidate column with the same names with the Counter subclass form Collections module
candidates = df['Candidate'].tolist()
counts = Counter(candidates)

#listing the summary count for each candidate "bucket" - Percentage formatting: https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python
for candidate, count in counts.items():
    print(f"{candidate}: {count/len(df.index):.3%} {count}")

print('--------------------------------------------------------------')

#Finding the number of times a value occurs and pulling the item with the highest number of occurances --> https://mode.com/python-tutorial/counting-and-plotting-in-python/ & https://www.w3schools.com/python/ref_func_max.asp

#defining the max count
max_count = max(counts.values())

#for loop pulling the value with the highest count from the set
for candidate, count in counts.items():
    if count == max_count:
        print(f"Winner: {candidate}")

print('--------------------------------------------------------------')

#Writing a txt file with all of my stuff - resources copied from the PyBank
file = r'C:\Users\lasot\OneDrive\Desktop\Data Bootcamp\Module 3 Python\PyPoll\Analysis\PyPollOutput.txt'

with open(file, 'w') as f:
    print('Election Results',file=f)
    print('--------------------------------------------------------------',file=f)
    print('Total Votes:', len(df.index),file=f)
    print('--------------------------------------------------------------',file=f)
    for candidate, count in counts.items():
        print(f"{candidate}: {count/len(df.index):.3%} {count}",file=f)
    print('--------------------------------------------------------------',file=f)
    for candidate, count in counts.items():
        if count == max_count:
            print(f"Winner: {candidate}",file=f)
    print('--------------------------------------------------------------',file=f)