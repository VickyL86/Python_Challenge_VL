# First we'll import the os module
# This will allow us to create file paths across operating systems --> from class Module
import csv
import os


# Module for reading CSV files --> from class module
import pandas as pd

#Thank you Dwight for the dirname(__file__) :D 
csvpath = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv") 

#Pull and read the file --> Thank you Dwight! 
df = pd.read_csv(csvpath)

print('Financial Analysis')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

#Get number of Months in the set = 
#Get number of rows less header --> https://sparkbyexamples.com/python/pandas-get-number-of-rows-examples/#:~:text=You%20can%20use%20len(df,()%20to%20get%20the%20count. 

print('Total Months:', len(df.index))

#create a sum of all values in the Prifit/Loss Column --> https://stackoverflow.com/questions/41286569/get-total-of-pandas-column
Total = df["Profit/Losses"].sum()

# Formatting from: https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators 
print(f"Total: ${Total:,}")


# Add another column with the rate of change using pandas df -->https://www.javatpoint.com/python-pandas-add-column-to-dataframe-columns & 
# https://www.statology.org/pandas-difference-between-rows/#:~:text=You%20can%20use%20the%20DataFrame,rows%20in%20a%20pandas%20DataFrame.&text=where%3A,rows%20for%20calculating%20the%20difference.
        
df['Average Change'] = df['Profit/Losses'].diff()

#getting average, min, & Max to print --> https://stackoverflow.com/questions/48847210/formula-for-the-average-of-the-change-in-a-column-of-numbers-from-row-to-row-in
average_change = df['Average Change'].mean()

#shorten the number format https://stackoverflow.com/questions/3914725/how-to-turn-a-float-number-like-293-4662543-into-293-47-in-python
print(f'Average Change: $ {average_change:,.2f}')

Max_Increase = df['Average Change'].max()

#pull by index ONLY - FIGURED IT OUT! - create a list from the 'Average Change' column in the df / loop through each value in the list via list comprehension 
# --> https://realpython.com/iterate-through-dictionary-python/
Change_list = [value for value in df['Average Change']] 

#pulling maximum value from average change list 
i_max = Change_list.index(Max_Increase)

print(f'Greatest Increase in Profits: {df["Date"][i_max]} (${Max_Increase:,.0f})')

#pulling minimum value from average change list 
Min_Increase = df['Average Change'].min()

#looking up index of the minimum from the column 
i_min = Change_list.index(Min_Increase)

print(f'Greatest Decrease in Profits: {df["Date"][i_min]} (${Min_Increase:,.0f})')

#Figuring out the export... --> Thank you Dwight!

file = os.path.join(os.path.dirname(__file__),"Analysis","Output.txt")

#export to txt success 
with open(file, 'w') as f:
    print('Financial Analysis',file=f)
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ',file=f)
    print('Total Months:', len(df.index),file=f)
    print(f"Total: ${Total:,}",file=f)
    print(f'Average Change: $ {average_change:,.2f}',file=f)
    print(f'Greatest Increase in Profits: {df["Date"][79]} (${Max_Increase:,.0f})',file=f)
    print(f'Greatest Decrease in Profits: {df["Date"][49]} (${Min_Increase:,.0f})',file=f)









