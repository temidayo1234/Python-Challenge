#Import operating system library and csv library 
import os
import csv

Month_Length = []
Profit_Losses = []
Diff_Arr = []
tracker = 0
Greatest_Increase = 0
Greatest_Decrease = Greatest_Increase
#Define the path of file and store in a variable
PyBankFile=os.path.join(".","Resources","budget_data.csv")
#Open file and store in a variable
with open(PyBankFile) as PyBankOpen:
    #Define variable to read through file 
    PyBankReader=csv.reader(PyBankOpen, delimiter=",")
    
    next(PyBankReader)

    for row in PyBankReader:   
        #Calculate total number of months 
        Month_Length.append(row[0])
        
        #Calculate total amount of profit and losses over entire period
        Profit_Losses.append(int(row[1]))
        Total_Profit_Losses = sum(Profit_Losses)   

    #Calculate average changes 
    for x in Profit_Losses:
        diff = int(x) - tracker
        tracker = x
        Diff_Arr.append(diff)  
    Average_Change = sum(Diff_Arr[1:]) / (len(Diff_Arr)-1)    

    #Calculate Greatest Increase
    for x in Diff_Arr:
        if x > Greatest_Increase:
            Greatest_Increase = x

    #Calculate Greatest Decrease
    for x in Diff_Arr:
        if x < Greatest_Decrease:
            Greatest_Decrease = x
    
    #Retrieve Month for Greatest Increase and Decrease
    for row in Month_Length:  
        if Month_Length.index(row)==Diff_Arr.index(Greatest_Increase):
            Greatest_Increase_Month = row
    for row in Month_Length:  
        if Month_Length.index(row)==Diff_Arr.index(Greatest_Decrease):
            Greatest_Decrease_Month = row
            print(Greatest_Decrease_Month)


    print("Finanial Analysis"/n)
    print("Finanial Analysis"/n)
    #print(len(Month_Length))
    #print(Total_Profit_Losses)
    #print(Average_Change)
    #print(Greatest_Increase)
    #print(Greatest_Decrease)
    
