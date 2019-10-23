# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

##############################################PARAMS
data = pd.read_csv('pasi.csv',header=None)
results=[]###this is your mean calculated for each subset of data
sds=[]
steps=[]#
max_steps = 21000#setting the stride. how many data points are included in every mean? e.g. 0 - 11000 are values for first mean
current_index=0#which index in the spreadsheet/dataframe are we atm
max_index=data.shape[0]-1#that is the last index we can query data from
counter=1
custom_steps=[11000,15000, 20000, 50000, 90000]###change these as u like, if you want custom spacing

#######################################################################################CODE
####################Use this line when U want to have evenly spaced means
#while current_index < max_index:

##############################use these lines INSTEAD if u want customly spaced means
 
for ind, currrent_index in enumerate(custom_steps):##########use this if u want to set steps manually! dont forget to comment out
    print('{} {}'.format(ind, currrent_index))
    try:
        max_steps = custom_steps[ind+1] - currrent_index
    except:
        max_steps = max_index - currrent_index   
#    
###################################################################################
    
    myRange=[]
    try:
        myRange= range(current_index,current_index+max_steps)
        temp_df= data[1].iloc[myRange]#gets data from column 1, queries the values we want to take the mean of. Alternatively u can query the data by its value
        
    except:#positional index out of bounds: last iteration did not have enough data points so we simply use whatever data is left
        myRange= range(current_index,max_index)
        temp_df= data[1].iloc[myRange]
        print('Reached end of the spreadsheet')
       
    results.append(temp_df.mean())
    sds.append(temp_df.std())
    steps.append(current_index+(max_steps/2))#get the step in the middle of our selected data. if only current step is used, u plot a sort of prospective restlt
    
    
    if counter%2 == 0:#plot section that has been analysed
        plt.plot(myRange, temp_df, color='black', linestyle='dashed', alpha=0.5)
    else:
        plt.plot(myRange, temp_df, color='gray', linestyle='dashed', alpha=0.3)
    
    counter+=1#to alternate colours
    current_index+=max_steps#update current starting index. Dont use this if u use
    
    
print('Means are: {}'.format(results)) 
print('SD are: {}'.format(sds))

plt.plot(steps, results, 'bx')#plot mean
#eb1 = plt.errorbar(steps, results,yerr=sds, uplims=True, lolims=True, markersize=7, fmt='o', color='b')  ###plot sds



