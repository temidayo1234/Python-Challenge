#Import operating system library and csv library 
import os
import csv

#Define the path of file and store in a variable
PyBankFile=os.path.join(".","Resources","budget_data.csv")
#Open file and store in a variable
with open(PyBankFile) as PyBankOpen:
    #Define variable to read through file 
    PyBankReader=csv.reader(PyBankOpen, delimiter=",")
    
    for row in PyBankReader:    
        print(row)