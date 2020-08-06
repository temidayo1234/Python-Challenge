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
PyBankFile=os.path.join("..","Resources","budget_data.csv")
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
    Formatted_Average_Change = "{:.2f}".format(Average_Change)

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
    #Print Results        
    print("Financial Analysis")
    print("---------------------")
    print("Total Months: " + str(len(Month_Length)))
    print("Total: " + str(Total_Profit_Losses))
    print("Average Change: " + str(Formatted_Average_Change))
    print("Greatest Increase in Profits: " + str(Greatest_Increase_Month) + " ($" + str(Greatest_Increase) + ")")
    print("Greatest Decrease in Profits: " + str(Greatest_Decrease_Month) + " ($" + str(Greatest_Decrease) + ")")
    

#Define the path of file and store in a variable
export_path = os.path.join("Results.csv")

#Open file and store in a variable
with open(export_path, 'w') as result_file:

    #Define variable to write in file 
    results_writer = csv.writer(result_file, delimiter=',')

    #Write results to file
    results_writer.writerow(["Financial Analysis"])
    results_writer.writerow(["---------------------"])
    results_writer.writerow(["Total Months: "] + [str(len(Month_Length))])
    results_writer.writerow(["Total: " ]+ [str(Total_Profit_Losses)])
    results_writer.writerow(["Average Change: "] + [str(Formatted_Average_Change)])
    results_writer.writerow(["Greatest Increase in Profits: " ]+ [str(Greatest_Increase_Month) + " ($" + str(Greatest_Increase) + ")"])
    results_writer.writerow(["Greatest Decrease in Profits: " ]+ [str(Greatest_Decrease_Month) + " ($" + str(Greatest_Decrease) + ")"])