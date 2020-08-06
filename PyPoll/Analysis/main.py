import os
import csv

Votes_Tendered = []
Candidates_Appearance = []
Unique_Candidates_List = []
Khan = []
Correy = []
Li = []
OTooley = []

#Define the path of file and store in a variable
PyPollFile=os.path.join("..","Resources","election_data.csv")

#Open file and store in a variable
with open(PyPollFile) as PyPollOpen:

    #Define variable to read through file 
    PyPollReader=csv.reader(PyPollOpen, delimiter=",")
    
    next(PyPollReader)
    
    #Read through the file
    for row in PyPollReader:

        #Caluclate total number of votes cast
        Votes_Tendered.append(row[0])

        #Store all apeareances of a candidate in a variable
        Candidates_Appearance.append(row[2])

        #Calculate total number of votes for each candidate. The list was known after retrieving the uniq appearance of candidates who recevied a vote
        if row[2]== 'Khan':
            Khan.append(row[0])
        if row[2]== 'Correy':
            Correy.append(row[0])
        if row[2]== 'Li':
            Li.append(row[0])
        if row[2]== 'O\'Tooley':
            OTooley.append(row[0])

    #Retrieve the unique appearance of candidates who recevied a vote
    for candidate in Candidates_Appearance:
        if candidate in  Unique_Candidates_List:
            continue
        Unique_Candidates_List.append(candidate)

    #Calculate percentage of votes cast
    Khan_Percentage = (len(Khan)/len(Votes_Tendered)) *100
    Formatted_Khan_Percentage = "{:.0f}".format(Khan_Percentage)
    Correy_Percentage = (len(Correy)/len(Votes_Tendered)) *100
    Formatted_Correy_Percentage = "{:.0f}".format(Correy_Percentage)
    Li_Percentage = (len(Li)/len(Votes_Tendered)) *100
    Formatted_Li_Percentage = "{:.0f}".format(Li_Percentage)
    OTooley_Percentage = (len(OTooley)/len(Votes_Tendered)) *100
    Formatted_OTooley_Percentage = "{:.0f}".format(OTooley_Percentage)
   
    #Calculate the winner
    if Formatted_Khan_Percentage > Formatted_Correy_Percentage and Formatted_Khan_Percentage > Formatted_Li_Percentage and Formatted_Khan_Percentage > Formatted_OTooley_Percentage:
        Winner = 'Khan'
    elif Formatted_Correy_Percentage > Formatted_Khan_Percentage and Formatted_Correy_Percentage > Formatted_Li_Percentage and Formatted_Correy_Percentage > Formatted_OTooley_Percentage:
        Winner = 'Correy'
    elif Formatted_Li_Percentage > Formatted_Correy_Percentage and Formatted_Li_Percentage > Formatted_Khan_Percentage and Formatted_Li_Percentage > Formatted_OTooley_Percentage:
        Winner = 'Li'
    elif Formatted_OTooley_Percentage > Formatted_Correy_Percentage and Formatted_OTooley_Percentage > Formatted_Khan_Percentage and Formatted_OTooley_Percentage > Formatted_Li_Percentage:
        Winner = 'O\'Tooley'

    #Print out all the results
    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(len(Votes_Tendered)))
    print("--------------------")   
    print(Unique_Candidates_List[0] + ": " + Formatted_Khan_Percentage + "%" + " (" + str(len(Khan)) + ")")
    print(Unique_Candidates_List[1] + ": " + Formatted_Correy_Percentage + "%" + " (" + str(len(Correy)) + ")")
    print(Unique_Candidates_List[2] + ": " + Formatted_Li_Percentage + "%" + " (" + str(len(Li)) + ")")
    print(Unique_Candidates_List[3] + ": " + Formatted_OTooley_Percentage + "%" + " (" + str(len(OTooley)) + ")") 
    print("--------------------")
    print("Winner: " + Winner)
    print("--------------------")

#Define the path of file and store in a variable
export_path = os.path.join("Results.csv")

#Open file and store in a variable
with open(export_path, 'w') as result_file:

    #Define variable to write in file 
    results_writer = csv.writer(result_file, delimiter=',')

    #Write results to file
    results_writer.writerow(["Election Results"])
    results_writer.writerow(["--------------------"])
    results_writer.writerow(["Total Votes: " + str(len(Votes_Tendered))])
    results_writer.writerow(["--------------------"])   
    results_writer.writerow([Unique_Candidates_List[0] + ": " + Formatted_Khan_Percentage + "%" + " (" + str(len(Khan)) + ")"])
    results_writer.writerow([Unique_Candidates_List[1] + ": " + Formatted_Correy_Percentage + "%" + " (" + str(len(Correy)) + ")"])
    results_writer.writerow([Unique_Candidates_List[2] + ": " + Formatted_Li_Percentage + "%" + " (" + str(len(Li)) + ")"])
    results_writer.writerow([Unique_Candidates_List[3] + ": " + Formatted_OTooley_Percentage + "%" + " (" + str(len(OTooley)) + ")"]) 
    results_writer.writerow(["--------------------"])
    results_writer.writerow(["Winner: "+ Winner])
    results_writer.writerow(["--------------------"])
 