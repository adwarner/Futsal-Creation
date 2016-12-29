# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:21:02 2016

@author: adamwarner
"""

## This program queries out the database 
## After the query it takes the values for each player and then 
## plots them on a barplot split between midfielders and attackers. 


import pandas as pd
import MySQLdb

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties


db = MySQLdb.connect(
        host = "localhost",
        user = "root",
        db = "test"
        )
cursor = db.cursor()
cursor.execute("""SELECT * from futsalData""")
data2 = cursor.fetchall ()
store = []
for row in data2 :
    store.append(row)

store = pd.DataFrame(store)



w = []
w_c = 0 

for j in range(len(store.columns)):
    for i in range(len(store)):
        if store[j][i]=='W':
            w.append(3)
        elif store[j][i]=='T':
            w.append(1)
        else: w.append(0)
            

#s.value_counts()

Buzz =pd.Series(store[0])
Buzz = Buzz.value_counts().sort_index()

Charlie =pd.Series(store[1])
Charlie = Charlie.value_counts().sort_index()

Dez =pd.Series(store[2])
Dez = Dez.value_counts().sort_index()

Henrik =pd.Series(store[3])
Henrik = Henrik.value_counts().sort_index()

Jose =pd.Series(store[4])
Jose = Jose.value_counts().sort_index()

Kevin =pd.Series(store[5])
Kevin = Kevin.value_counts().sort_index()

Matt =pd.Series(store[6])
Matt = Matt.value_counts().sort_index()

Mitch =pd.Series(store[7])
Mitch = Mitch.value_counts().sort_index()

Nate =pd.Series(store[8])
Nate = Nate.value_counts().sort_index()

Reid =pd.Series(store[9])
Reid = Reid.value_counts().sort_index()

Rico =pd.Series(store[10])
Rico = Rico.value_counts().sort_index()

Scud =pd.Series(store[11])
Scud = Scud.value_counts().sort_index()

Snider =pd.Series(store[12])
Snider = Snider.value_counts().sort_index()

Tanner =pd.Series(store[13])
Tanner = Tanner.value_counts().sort_index()

Tim = pd.Series(store[14])
Tim = Tim.value_counts().sort_index()

Toby =pd.Series(store[15])
Toby = Toby.value_counts().sort_index()

Tyler =pd.Series(store[16])
Tyler = Tyler.value_counts().sort_index()

Will =pd.Series(store[17])
Will = Will.value_counts().sort_index()

Zo =pd.Series(store[18])
Zo = Zo.value_counts().sort_index()




N = 8
Defender_Losses = (Dez[0], Henrik[0], Tyler[0], Scud[0], Tim[0], Mitch[0], Rico[0],Tanner[0])

ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, Defender_Losses, width, label = 'losses', color='r')

Defender_Wins = (Dez[2], Henrik[2], Tyler[2], Scud[2], Tim[2], Mitch[2], Rico[2],Tanner[2])
rects2 = ax.bar(ind+2*width, Defender_Wins, width,label = 'wins', color='gray')

Defender_Ties = (Dez[1], Henrik[1], Tyler[1], Scud[1], Tim[1], Mitch[1], Rico[1], Tanner[2])
rects3 = ax.bar(ind+width, Defender_Ties, width,label = 'ties', color='b')

#womenMeans = (25, 32, 34, 20, 25)
#rects2 = ax.bar(ind+width, womenMeans, width, color='y')

# add some
ax.set_ylabel('')
ax.set_title('Defenders Win, Losses, Ties')
ax.set_xticks(ind+1.5*width)
ax.set_xticklabels( ('Dez', 'Henrik', 'Tyler', 'Scudder', 'Tim','Mitch','Rico', 'Tanner') )


#ax.legend( (rects1[0], rects2[0], rects3[0]), ('Loss','Wins','Ties') )
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1))
ax.grid('on')
fig.savefig('Defenders', bbox_extra_artists=(lgd,), bbox_inches='tight')


plt.show()


N = 8
Attacker_Losses = (Buzz[0],Jose[0], Kevin[0], Snider[0], Reid[0], Nate[0],Toby[0], Zo[0])

ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, Attacker_Losses, width, color='r', label = 'Losses')

Attacker_Wins = (Buzz[2],Jose[2], Kevin[2], Snider[2], Reid[2], Nate[2],Toby[2], Zo[2])
rects2 = ax.bar(ind+2*width, Attacker_Wins, width, color='gray', label = 'Wins')

Attacker_Ties = (Buzz[1],Jose[1], Kevin[1], Snider[1], Reid[1], Nate[1],Toby[1], Zo[1])
rects3 = ax.bar(ind+width, Attacker_Ties, width, color='b', label = 'Ties')

#womenMeans = (25, 32, 34, 20, 25)
#rects2 = ax.bar(ind+width, womenMeans, width, color='y')

# add some
ax.set_ylabel('')
ax.set_title('Midfielder/Attackers Win, Losses, Ties')
ax.set_xticks(ind+1.5*width)
ax.set_xticklabels( ('Buzz','Jose', 'Kevin', 'Snider', 'Reid', 'Nate','Toby','Zo') )

handles, labels = ax.get_legend_handles_labels()

lgd1 = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1))
ax.grid('on')
fig.savefig('Attackers', bbox_extra_artists=(lgd1,), bbox_inches='tight')

plt.show()

db.close()