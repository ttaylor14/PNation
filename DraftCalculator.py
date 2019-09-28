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


# Temporary Team Place Holder
tempdf = []
avail_faab = 0
full_roster = pd.read_csv('data/FullRoster.csv')
full_roster = full_roster.iloc[0:0]
print(full_roster)



####################

#### Import Data ###

####################


# import files
rosters = pd.read_csv('data/FullRoster.csv')
team_info = pd.read_csv('data/Teams/team_info.csv')

# Rename col "Player Salary" to salary
rosters.rename(columns={'Player Salary':'salary'}, inplace=True)


# Pull Team Info
temp_faab = pd.read_csv('data/Teams/team_info.csv')
# print(temp_faab)

# Deletd row with no name and are not begin kept
rosters['Player'].replace('', np.nan, inplace=True)
rosters['salary'].replace('', np.nan, inplace=True)
rosters['Keeping'].replace('', np.nan, inplace=True)
rosters.dropna(subset=['Player'], inplace=True)
rosters.dropna(subset=['salary'], inplace=True)
rosters.dropna(subset=['Keeping'], inplace=True)

# Removes all Player Salaries less than 1
rosters = rosters[rosters['salary'] > 1]

team_info = team_info.set_index("team_id", drop=False)

# convert columns to correct types
rosters[['team_id', 'salary']] = rosters[['team_id', 'salary']].apply(pd.to_numeric)
team_info[['team_id', 'faab']] = team_info[['team_id', 'faab']].apply(pd.to_numeric)

# print(rosters.head())
# print(team_info.head())

########################################

### Confirm League Settings Function ###

########################################

# This function will be used to confirm all settings
# For the draft. This will be done at the execution of
# Draft Prep Function to confirm settings.

# should make one question to confirm all attributes
# Question not working??


def settings_confirm():
    while True:
        qr = input('Is the Draft Budget $300')
        if qr == '' or not qr[0].lower() in ['y', 'n']:
            print('Please answer with yes or no!')
        else:
            break
    if qr[0].lower() == 'y':  # go to next question
        return
    if qr[0].lower() == 'n':
        print("update draft_budget value")
        return

# test function
# settings_confirm()

######################################

### Confirm Team Settings Function ###

######################################

# This function will be used to confirm Team Settings
# This will include lineup sizes, faab balances, etc...


def team_settings(id):
    global tempdf
    global avail_faab

    avail_faab = team_info.loc[id, 'faab']
    tempdf = rosters.loc[rosters['team_id'] == id]
    print(avail_faab)
    print(tempdf)

# test function
# team_settings(5)


#################################

#### Calculate Draft Salaries ###

#################################

# FAAB Reducation
# Reducing Player Salaries with remaining FAAB

# next step is to run this code with the df - check
# then create loop to run through for each team.... - check
# then apply same info to the keeper salary function - check
# replace add salary function's salary reduction code with the actual salary reduction function - check
# check fluidity that the calculations build on one another and salaries are updated in the csv file
# send results to csv output files (overwrite)
# do this with out being applied to csv file until after it is committed??
# write seperate file to merge all team rosters into the single roster file?
#   - or rewrite file imports to pull all individual team rosters within??
# add keeper selection ability - marked column

# Once everything is running smoothly, remove unnesscesary prints
# and clean up out put and create a log file! - print records to a log file?
# or two print outs to different log files?


################################

#### FAAB Reduction Function ###

################################


# Remove temp_list element and update the actual tempdf object instead
# This will eliminate the need for applying the temp_list values as replacements for salaries
# Apply Tempdf to csv?

def Faab_Reduction(id):
    global tempdf
    global avail_faab

    print("You current have: $" + str(avail_faab) + " of FAAB Remaining")
    print("Current Roster: ")

    # sum needs to be checked to ensure team can afford players for draft

    i = 0

    while avail_faab > 0:
                                          # If you have faab
        while tempdf['salary'].sum() < len(tempdf.index):              # if the sum of all salaries is greater than the number of players (all $1)

            while int(tempdf.salary.iloc[[i]]) >= 0:
                if int(tempdf.salary.iloc[[i]]) == 1:                   # when a salary = 1 skip
                    i = i + 1
                    if i >= (len(tempdf.index)):                           # when we reach the last entry
                        i = 0
                    break

                if int(tempdf.salary.iloc[[i]]) > 1:
                    if avail_faab > 0:
                        avail_faab = avail_faab - 1                       # reduce faab
                        new_sal = int(tempdf.salary.iloc[[i]]) - 1        # reduce salary of dataframe
                        tempdf.salary.iloc[[i]] = new_sal                 # apply new Salary to temp datafram
                        #tempdf.iloc[tempdf.iloc[i], "salay"] = int(tempdf.salary.iloc[[i]]) - 1
                        i = i + 1                                         # next entry
                        print("my faab" + str(avail_faab))              # Print Available Faab
                        print(tempdf)                                   # Prints Temp Dataframe
                        if i >= (len(tempdf.index)):                      # when we reach the last entry
                            i = 0 # reset to 0

        else:
            print("Salaries are all $1")
            print("Team ID: " + str(id))
            print(tempdf)
            break

    else:
        print("Out of FAAb")
        print("Team ID: " + str(id))
        print(tempdf)


# test function
# Faab_Reduction(5)


##############################

#### Keeper Costs Function ###

##############################


def Add_Keeper_Salaries(id):

    global keeper_cost
    global faab_reduction
    global keeper_cost_reduction
    global tempdf

    print("You current have: $" + str(avail_faab) + " of FAAB Remaining")
    print("Current Roster: ")

    tempdf['salary'] = (tempdf['salary'] + keeper_cost)       # Keeper Cost is applied to salaries
    print("Team ID: " + str(id))
    print(tempdf)


#################################

#### Calculate Draft Salaries ###

#################################

def draft_budget():
    return


# test function
# draft_budget()

######################################

### create Team Rosters by team_id ###

######################################

def tempdf_rosters():

    global full_roster
    global tempdf

    # Build full Roster Page

    # merge dataframes
    # full_roster = full_roster.append(tempdf, ignore_index=True, sort=False)
    full_roster = pd.concat([full_roster, tempdf])
    print("Final Team Rosters for the Draft:")
    print(full_roster)


def tempdf_faab():

    global temp_faab
    global tempdf

    # Build full Roster Page

    # merge dataframes
    # full_roster = full_roster.append(tempdf, ignore_index=True, sort=False)
    temp_faab = pd.concat([temp_faab, tempdf])
    print("Final Team faab for the Draft:")
    print(temp_faab)

    # replace faab...


def update_rosters():

    global full_roster

    # This should be a seperate function that takes the full_roster and divides it out one the for loop is complete.

    # create each team
    team_1 = full_roster[full_roster['team_id'] == 1]
    team_2 = full_roster[full_roster['team_id'] == 2]
    team_3 = full_roster[full_roster['team_id'] == 3]
    team_4 = full_roster[full_roster['team_id'] == 4]
    team_5 = full_roster[full_roster['team_id'] == 5]
    team_6 = full_roster[full_roster['team_id'] == 6]
    team_7 = full_roster[full_roster['team_id'] == 7]
    team_8 = full_roster[full_roster['team_id'] == 8]
    team_9 = full_roster[full_roster['team_id'] == 9]
    team_10 = full_roster[full_roster['team_id'] == 10]
    team_11 = full_roster[full_roster['team_id'] == 11]
    team_12 = full_roster[full_roster['team_id'] == 12]
    team_13 = full_roster[full_roster['team_id'] == 13]
    team_14 = full_roster[full_roster['team_id'] == 14]

# at the end export each team to own file in teams Folder
    team_1.to_csv('data/Teams/Team1.csv', encoding='utf-8', index=False)
    team_2.to_csv('data/Teams/Team2.csv', encoding='utf-8', index=False)
    team_3.to_csv('data/Teams/Team3.csv', encoding='utf-8', index=False)
    team_4.to_csv('data/Teams/Team4.csv', encoding='utf-8', index=False)
    team_5.to_csv('data/Teams/Team5.csv', encoding='utf-8', index=False)
    team_6.to_csv('data/Teams/Team6.csv', encoding='utf-8', index=False)
    team_7.to_csv('data/Teams/Team7.csv', encoding='utf-8', index=False)
    team_8.to_csv('data/Teams/Team8.csv', encoding='utf-8', index=False)
    team_9.to_csv('data/Teams/Team9.csv', encoding='utf-8', index=False)
    team_10.to_csv('data/Teams/Team10.csv', encoding='utf-8', index=False)
    team_11.to_csv('data/Teams/Team11.csv', encoding='utf-8', index=False)
    team_12.to_csv('data/Teams/Team12.csv', encoding='utf-8', index=False)
    team_13.to_csv('data/Teams/Team13.csv', encoding='utf-8', index=False)
    team_14.to_csv('data/Teams/Team14.csv', encoding='utf-8', index=False)


# create roster file by combining all team files
# once all individual files are made recombing and save over old roster file, in a seperate py file?

# test function
# update_rosters()

def clean_df():

    global tempdf
    global avail_faab

    tempdf = []
    avail_faab = 0


############################

#### Draft Prep Function ###

############################

# This function will cycle through all required functions
# In preperation for the Draft.

def draft_prep():

    # Step 1: Confirm League Settings
    # settings_confirm()

    # Step 2: Confirm Team Settings
    # team_settings(id)

    # Step 3: Faab Reduction
    for id in team_info['team_id']:

        team_settings(id)

        Faab_Reduction(id)

        # Step 4: Keeper Costs
        Add_Keeper_Salaries(id)

        # Salary Reduction after Keeper Costs are applied
        if keeper_cost_reduction == "on":
            Faab_Reduction(id)

        if keeper_cost_reduction == "off":
            # this skips Faab Reduction after Keeper Costs
            pass

        else:
            pass

        # Step 5: Draft Budgets
        # draft_budget()

        # Step 6: Add new df to full_roster
        tempdf_rosters()

        # Step 7: Update Team Files with Accurate Information
        update_rosters()

        # Step 8: Clean Global Variables for next team
        # clean_df()

    # This will only update individual team files
    # Not the Roster File


#################################

#### Finalize Teams for Draft ###

#################################

# the following function will complete all draft prep work
# this will be irreversible and must be take with extreme caution.

draft_prep()


