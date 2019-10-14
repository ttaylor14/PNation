# Creating Roto Rankings

# last Update : 10.13.19

# Helpful resource: https://fantasysixpack.net/creating-fantasy-baseball-player-rater/

# Current Roto Rankings needs adjustment to account for stat accumulation


import pandas as pd
import numpy as np


# Pull Data
roto = pd.read_csv('data/Roto_Current_Total_Rankings.csv')
points = pd.read_csv('data/Rankings.csv')


roto = roto[['Roto_Rank', 'Total_Z', 'Name', 'Team', 'Age']]
points = points[['Rank', 'Total_Points', 'Name_bat', 'Team_bat', 'Age_bat']]


Rankings =  pd.merge(roto, points, left_on=['Name', 'Age', 'Team'], right_on=['Name_bat', 'Age_bat', 'Team_bat'], how='inner')

Difference = Rankings['Roto_Rank'] - Rankings['Rank']

Rankings.insert(0, 'Difference', Difference)

Rankings = Rankings.sort_values('Total_Z', ascending=False)

Rankings = Rankings[['Roto_Rank', 'Rank', 'Difference', 'Name', 'Team', 'Age', 'Total_Z', 'Total_Points']]

Rankings.rename(columns={'Rank':'Points_Rank'}, inplace=True)

Rankings.to_csv('data/Roto_Points_Difference.csv', sep=',', index=False, encoding='utf-8')



Difference['Difference'] = Rankings['Points_Rank'] - Rankings['Roto_Rank']


Rankings = Rankings[['Points_Rank', 'Roto_Rank', 'Difference', 'Name', 'Team', 'Age', 'Total_Points', 'Total_Z']]

Rankings = Rankings.sort_values('Points_Rank', ascending=True)

Rankings.to_csv('data/Points_Roto_Difference.csv', sep=',', index=False, encoding='utf-8')


print("Success")
