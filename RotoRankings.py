# Creating Roto Rankings

# last Update : 9.29.19

# Helpful resource: https://fantasysixpack.net/creating-fantasy-baseball-player-rater/

# Current Roto Rankings needs adjustment to account for stat accumulation


import pandas as pd
import numpy as np



def Stat_cat():
    global rotoCat
    rotoCat = [BA, R, RBI, HR, SB, K, ERA, WHIP, Saves, Wins]
    return rotoCat



def roto_Rankings():
    global rotoCat

    # Pull Data
    roster = pd.read_csv('data/Rankings.csv')

    # Create Required Columns
    names = ['Season_bat', 'Total_Points', 'Name_bat', 'Team_bat', 'Age_bat']
    rotoCat = ['BA', 'R', 'RBI', 'HR', 'SB', 'K', 'ERA', 'WHIP', 'Saves', 'Wins']
    rotoCol = names + rotoCat
    # print(rotoCol)

    # Create needed Columns
    roster['BA'] = roster['AVG_bat']
    roster['R'] = roster['R_bat']
    roster['RBI'] = roster['RBI_bat']
    roster['HR'] = roster['HR_bat']
    roster['SB'] = roster['SB_bat']
    roster['K'] = roster['SO_pit']
    roster['ERA'] = roster['ERA_pit']
    roster['WHIP'] = ( roster['BB_pit'] + roster['H_pit'] ) / roster['IP_pit']
    roster['Saves'] = roster['SV_pit']
    roster['Wins'] = roster['W_pit']

    # print(roster.head())


    #### how to make ERA and WHIP better for a lower number vs a higher....

    # Limit Data to specific Columns
    roster = roster[rotoCol]
    # print(roster.head())

    # Create Z score for each Roto Cat
    for col in rotoCat:
        col_zscore = col + '_zscore'
        roster[col_zscore] = (roster[col] - roster[col].mean())/roster[col].std(ddof=0)

    # print(roster.head())

    # Fill all NA with 0 to eliminate adding errors
    roster.fillna(0)

    # Calculate Total Z Score for Rankings
    roster['Total_Z'] = roster['BA_zscore'] + roster['R_zscore'] + roster['RBI_zscore'] + roster['HR_zscore'] + roster['SB_zscore'] + roster['K_zscore'] + roster['ERA_zscore'] + roster['WHIP_zscore'] + roster['Saves_zscore'] + roster['Wins_zscore']
    # print(roster['Total_Z'])

    # Create Roto Rankings based on overall Z Score
    roster = roster.sort_values('Total_Z', ascending=False)
    roster = roster.reset_index(drop=True)
    Rank = roster.index
    roster.insert(0, 'Roto_Rank', Rank)

    # print(roster.head())


    # Send Results to CSV
    roster.to_csv('data/Roto_Current_Rankings.csv', sep=',', index=False, encoding='utf-8')

    print("Success")

roto_Rankings()




