# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:10:53 2016

@author: adamwarner
"""
import numpy as np 
import pandas as pd
data_names = ['Nate','Tyler','Reid',
         'Toby','Henrik','Snider','Zo',
         'Tanner','Jose','Dez','Rico',
         'Tim','Scud','Mitch','Kevin','Buzz', 'Will','Charlie','Matt']
         
names = ['Nate','Tyler','Reid',
         'Toby','Henrik','Snider','Zo',
         'Tanner','Jose','Dez','Rico',
         'Adam','Noah','Tim','Scud','Mitch','Kevin',"Mark"]
         
gk = ['Will','Charlie','Matt']
teams = np.random.choice(names,size=(3,6),replace=False)
gk_1 = np.random.choice(gk,size=(3,1),replace=False)
gk_1 =pd.DataFrame(gk_1)
# Create three seperate teams 
# Remember python indexes with 0 
teams = pd.DataFrame(teams)
teams = pd.concat([teams,gk_1],axis = 1,ignore_index = True)

team1 = pd.DataFrame(teams.iloc[0])
team2 = pd.DataFrame(teams.iloc[1])
team3 = pd.DataFrame(teams.iloc[2])

print team1
print team2 
print team3 

                    

#for i in range(19): 
#  if (df.iloc[0,i] in ['Buzz','Zo']) == True:
#    print i
#  i += 1

not_here = []
for i in range(len(data_names)): 
    if (data_names[i] in names+gk)== False:
        not_here.append(data_names[i])
        print not_here
        
#count = 0
#for i in range(len(df.columns)):
#    if (df.iloc[0,i] in not_here) == False:
#        for j in range(len(team1_score.columns)):
#            df.iloc[j+1,count] == "Hello"
#    count += 1
#    