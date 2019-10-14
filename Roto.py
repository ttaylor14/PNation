# Creating Roto Rankings

# last Update : 10.13.19

# Helpful resource: https://fantasysixpack.net/creating-fantasy-baseball-player-rater/

# Current Roto Rankings needs adjustment to account for stat accumulation


import pandas as pd
import numpy as np



def Stat_cat():
    global rotoCatBat
    global rotoCatPit
    rotoCatBat = [BA, R, RBI, HR, SB]
    rotoCatPit = [K, ERA, WHIP, Saves, Wins]
    return rotoCatBat, rotoCatPit



def roto_Rankings():
    global rotoCatBat
    global rotoCatPit

    # Pull Data
    rosterB = pd.read_csv('data/bstats.csv')
    rosterP = pd.read_csv('data/pstats.csv')

    # Create Required Columns
    names = ['Season', 'Points', 'Name', 'Team', 'Age']
    rotoCatBat = ['BA', 'R', 'RBI', 'HR', 'SB']
    rotoCatPit = ['K', 'ERA', 'WHIP', 'Saves', 'Wins']
    rotoColBat = names + rotoCatBat
    rotoColPit = names + rotoCatPit
    # print(rotoCol)

    # Create needed Columns
    rosterB['BA'] = rosterB['AVG']
    rosterB['R'] = rosterB['R']
    rosterB['RBI'] = rosterB['RBI']
    rosterB['HR'] = rosterB['HR']
    rosterB['SB'] = rosterB['SB']
    rosterP['K'] = rosterP['SO']
    rosterP['ERA'] = rosterP['ERA']
    rosterP['WHIP'] = ( rosterP['BB'] + rosterP['H'] ) / rosterP['IP']
    rosterP['Saves'] = rosterP['SV']
    rosterP['Wins'] = rosterP['W']


    # Needed for Modified Z-Score
    rosterTempB = pd.DataFrame()
    rosterTempP = pd.DataFrame()
    rosterTempB['AB'] = rosterB['AB']
    rosterTempP['IP'] = rosterP['IP']

    # print(roster.head())


    #### how to make ERA and WHIP better for a lower number vs a higher....

    # Limit Data to specific Columns
    rosterB = rosterB[rotoColBat]
    rosterP = rosterP[rotoColPit]
    # print(roster.head())

    # Create Z score for each Roto Cat
    for col in rotoCatBat:
        col_zscore = col + '_zscore'
        rosterB[col_zscore] = (rosterB[col] - rosterB[col].mean())/rosterB[col].std(ddof=0)

    for col in rotoCatPit:
        col_zscore = col + '_zscore'
        rosterP[col_zscore] = (rosterP[col] - rosterP[col].mean())/rosterP[col].std(ddof=0)

    # print(roster.head())

    # Fill all NA with 0 to eliminate adding errors
    rosterB.fillna(0)
    rosterP.fillna(0)

    # Calculate Total Z Score for Rankings
    ZTotalB = rosterB['BA_zscore'] + rosterB['R_zscore'] + rosterB['RBI_zscore'] + rosterB['HR_zscore'] + rosterB['SB_zscore']
    ZTotalP = rosterP['K_zscore'] - rosterP['ERA_zscore'] - rosterP['WHIP_zscore'] + rosterP['Saves_zscore'] + rosterP['Wins_zscore']

    rosterB.insert(2, 'Total_Z', ZTotalB)
    rosterP.insert(2, 'Total_Z', ZTotalP)

    ZTotalBModified = ( rosterTempB['AB'] * ZTotalB - rosterTempB['AB'].mean() ) / rosterP['Total_Z'].std(ddof=0)
    ZTotalPModified = ( rosterTempP['IP'] * ZTotalB - rosterTempP['IP'].mean() ) / rosterP['Total_Z'].std(ddof=0)


    #Insert Modified Z-Score to account for player contribution
    rosterB.insert(2, 'Total_Zn', ZTotalBModified)
    rosterP.insert(2, 'Total_Zn', ZTotalPModified)

    # print(roster['Total_Z'])

    # Create Roto Rankings based on overall Z Score
    rosterB = rosterB.sort_values('Total_Z', ascending=False)
    rosterB = rosterB.reset_index(drop=True)
    Rank = rosterB.index
    rosterB.insert(0, 'Roto_Rank_Bat', Rank)

    rosterP = rosterP.sort_values('Total_Z', ascending=False)
    rosterP = rosterP.reset_index(drop=True)
    Rank = rosterP.index
    rosterP.insert(0, 'Roto_Rank_Pit', Rank)

    # print(roster.head())


    # Send Results to CSV
    rosterB.to_csv('data/Roto_Current_Bat_Rankings.csv', sep=',', index=False, encoding='utf-8')
    rosterP.to_csv('data/Roto_Current_Pit_Rankings.csv', sep=',', index=False, encoding='utf-8')


    Rankings =  pd.merge(rosterB, rosterP, how='outer')

    Rankings = Rankings.sort_values('Total_Z', ascending=False)
    Rankings = Rankings.reset_index(drop=True)
    Rank = Rankings.index
    Rankings.insert(0, 'Roto_Rank', Rank)
    Rankings.to_csv('data/Roto_Current_Total_Rankings.csv', sep=',', index=False, encoding='utf-8')


    print("Success")

roto_Rankings()




