#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies
import os
import csv


# In[2]:


#set path
PyPoll = os.path.join("election_data.csv")


# In[3]:


#create empty lists for later
candidates = []
vote_count = []


# In[4]:


with open(PyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #fill empty list with columns from data and obtain how many votes each got
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count.append(1)
        else:
            whatindex = candidates.index(row[2])
            vote_count[whatindex] += 1
    #Find total votes
    total_votes = sum(vote_count)
    #find percentage for each candidate
    votepercentage = [round(vote_count[i]/total_votes*100,4) for i in range(0,len(vote_count))]
    #print using lists and variables gathered above
    print(" Election Results ")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    
    for i in range(0,len(candidates)):
        print(f"{candidates[i]}: {votepercentage[i]}% ({vote_count[i]})")

    print("------------------------")
    print(f"Winner: {candidates[vote_count.index(max(vote_count))]}")
    #create text file
    with open("pollOutput.txt", "w") as text_file:
        print(" Election Results ", file=text_file)
        print("------------------------", file=text_file)
        print(f"Total Votes: {total_votes}", file=text_file)
        print("------------------------", file=text_file)
        for i in range(0,len(candidates)):
            print(f"{candidates[i]}: {votepercentage[i]}% ({vote_count[i]})", file=text_file)
        print("------------------------", file=text_file)
        print(f"Winner: {candidates[vote_count.index(max(vote_count))]}", file=text_file)


# In[ ]:





# In[ ]:




