# Draft Calculator File

# last Update : 9.28.19

#### To Do:
# update info to match FullRoster.csv label changes
# ensure faab works properly
# Ensure program would work with decimals...

import pandas as pd
import numpy as np


##################################

#### Master attribute controls ###

##################################

keeper_cost = 5         # How much keepers bonus costs
draft_budget = 300      # Upcoming Draft Budget
roster_spots = 25       # Max number of Keepers (roster spots)
il_spots = 5            # Max number of Injured Reserves Spots

# faab reduction - how much player salaries are decreased per dollar of faab
faab_reduction = 1      # how much salary reduction is applied per $1 of faab applied

# turn keeper cost reduction on or off
# if 'on' faab will reduce keeper costs

keeper_cost_reduction = 'on'
# keeper_cost_reduction = 'off'




##############################

#### Import Team Info Data ###

##############################


# import files
team_info = pd.read_csv('data/Teams/team_info.csv')

# Find team_id
team_info = team_info.set_index("team_id", drop=False)


team_info[['team_id', 'faab']] = team_info[['team_id', 'faab']].apply(pd.to_numeric)

teamNumber = 5 # team_id#


print(team_info.head())


################################

#### FAAB Reduction Function ###

################################

def Faab_Reduction(id, avail_faab):

    print("You current have: $" + str(avail_faab) + " of FAAB Remaining")
    print("Current Roster: ")

    # sum needs to be checked to ensure team can afford players for draft

    i = 0

    while avail_faab > 0:
                                          # If you have faab
        while roster['salary'].sum() < len(roster.index):              # if the sum of all salaries is greater than the number of players (all $1)

            while int(roster.salary.iloc[[i]]) >= 0:
                if int(roster.salary.iloc[[i]]) == 1:                   # when a salary = 1 skip
                    i = i + 1
                    if i >= (len(roster.index)):                           # when we reach the last entry
                        i = 0
                    break

                if int(roster.salary.iloc[[i]]) > 1:
                    if avail_faab > 0:
                        avail_faab = avail_faab - 1                       # reduce faab
                        new_sal = int(roster.salary.iloc[[i]]) - 1        # reduce salary of dataframe
                        roster.salary.iloc[[i]] = new_sal                 # apply new Salary to temp datafram

                        i = i + 1                                         # next entry
                        print("my faab" + str(avail_faab))              # Print Available Faab
                        print(roster)                                   # Prints Temp Dataframe
                        if i >= (len(roster.index)):                      # when we reach the last entry
                            i = 0 # reset to 0

        else:
            print("Salaries are all $1")
            print("Team ID: " + str(id))
            print(roster)
            break

    else:
        print("Out of FAAb")
        print("Team ID: " + str(id))
        print(roster)




################################

#### Import Team Roster Data ###

################################

filename = "data/Teams/Team%s.csv" % teamNumber
roster = pd.read_csv(filename)


# Rename col "Player Salary" to salary
roster.rename(columns={'Player Salary':'salary'}, inplace=True)

# Deletd row with no name and are not begin kept
roster['Player'].replace('', np.nan, inplace=True)
roster['salary'].replace('', np.nan, inplace=True)
roster['Keeping'].replace('', np.nan, inplace=True)
roster.dropna(subset=['Player'], inplace=True)
roster.dropna(subset=['salary'], inplace=True)
roster.dropna(subset=['Keeping'], inplace=True)

roster = roster.drop(columns=['lahmanID', 'retroID', 'bbrefID', 'Trade Block'])

# Removes all Player Salaries less than 1
roster = roster[roster['salary'] > 1]

# convert columns to correct types
roster[['team_id', 'salary']] = roster[['team_id', 'salary']].apply(pd.to_numeric)

print(roster.head())

faab = team_info.loc[team_info['team_id'] == teamNumber, 'faab'].iloc[0]
print(faab)


Faab_Reduction(teamNumber, faab)
