# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:35:26 2016

@author: adamwarner
"""
import pandas as pd 
import numpy as np
import MySQLdb

#Must run team_generation first! 

team_size = len(team1)

team1_score = pd.DataFrame(['W','T','W','L'])

team1_score = pd.DataFrame.transpose(team1_score)
team1_score = pd.concat([team1_score]*team_size,ignore_index = True)

team2_score = pd.DataFrame(['L','W','T','W'])
team2_score = pd.DataFrame.transpose(team2_score)
team2_score = pd.concat([team2_score]*team_size,ignore_index = True)


team3_score = pd.DataFrame(['T','W','L','W'])
team3_score = pd.DataFrame.transpose(team3_score)
team3_score = pd.concat([team3_score]*team_size,ignore_index = True)


team1_data = pd.concat([team1,team1_score],axis =1, join = 'inner',ignore_index = True)
team2_data = pd.concat([team2,team2_score],axis =1, join = 'inner',ignore_index = True)
team3_data = pd.concat([team3,team3_score],axis =1, join = 'inner',ignore_index = True)


todays_data = pd.concat([team1_data,team2_data,
                         team3_data],axis = 0, ignore_index = True)

todays_data = todays_data.sort(columns = [0])   
df = pd.DataFrame(todays_data)

if not not not_here: 
    testz = np.random.choice(['Z']*len(team1_score.columns)*len(not_here),
                     size = (len(not_here),len(team1_score.columns)))
    testz = pd.DataFrame(testz)
    not_herez = pd.DataFrame(not_here)
    not_here_data = pd.concat([not_herez,testz], axis = 1, ignore_index=True)


    df = df.sort(columns = [0])
    
    df = pd.concat([df,not_here_data], axis = 0, ignore_index = True)

df = pd.DataFrame.transpose(df)

data = []

test = []
for i in range(len(todays_data[0])):
    test.append(todays_data[0].values[i])

count = 0
for i in range(len(test)): 
    if (test[i] in data_names) == False:
        df.iloc[0,count]="Senior"
    count += 1

df  = pd.DataFrame.transpose(df)
df = pd.DataFrame(df[df[0] != 'Senior'])
df = df.sort(columns = [0])
df = pd.DataFrame.transpose(df)


for row in range(len(df)):
    if row > 0:
#    """name is in the 0th col. email is the 4th col."""
        Buzz = df.iloc[row,0]        
        Charlie = df.iloc[row,1]
        Dez = df.iloc[row,2]
        Henrik = df.iloc[row,3]
        Jose = df.iloc[row,4]
        Kevin = df.iloc[row,5]
        Matt = df.iloc[row,6]
        Mitch = df.iloc[row,7]
        Nate = df.iloc[row,8]
        Reid = df.iloc[row,9]
        Rico = df.iloc[row,10]
        Scud = df.iloc[row,11]
        Snider = df.iloc[row,12]
        Tanner = df.iloc[row,13]
        Tim = df.iloc[row,14]
        Toby = df.iloc[row,15]
        Tyler = df.iloc[row,16]
        Will = df.iloc[row,17]
        Zo = df.iloc[row,18]
        
        data.append((Buzz,Charlie,Dez,Henrik,Jose,Kevin,Matt,Mitch,Nate,Reid,Rico,
                     Scud,Snider,Tanner,Tim,Toby,Tyler,Will,Zo))

#db = MySQLdb.connect(host=host, user=user, db=dbname, passwd=pwd)

db = MySQLdb.connect(
        host = "localhost",
        user = "root",
        db = "test"
        )
cursor = db.cursor()
cursor.executemany("""INSERT INTO futsaldata (Buzz, Charlie,Dez,Henrik,Jose,Kevin,Matt,Mitch,Nate,Reid,Rico,
                     Scud,Snider,Tanner,Tim,Toby,Tyler,Will,Zo) VALUES (%s,%s,
                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                     ,%s,%s,%s)""", data)
db.commit()
#cursor.execute("""SELECT * from futsalData""")
#data2 = cursor.fetchall ()
#for row in data2 :
#    print row[0], row[1]

db.close()








