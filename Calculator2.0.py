## PNation.py

import pandas as pd


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
#keeper_cost_reduction = 'off'



####################

#### Import Data ###

####################

# import files
rosters = pd.read_csv('data/rosters.csv') 
team_info = pd.read_csv('data/team_info.csv') 

team_info = team_info.set_index("team_id", drop = False)

# convert columns to correct types
rosters[['team_id','roster_id','salary']] = rosters[['team_id','roster_id','salary']].apply(pd.to_numeric)
team_info[['team_id','faab']] = team_info[['team_id','faab']].apply(pd.to_numeric)

#print(rosters.head())
#print(team_info.head())

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
        if qr == '' or not qr[0].lower() in ['y','n']:print('Please answer with yes or no!')
        else:break
    if qr[0].lower() == 'y': # go to next question
        return
    if qr[0].lower() == 'n':
        print ("update draft_budget value")
        return

# test function
# settings_confirm()


#################################

#### Calculate Draft Salaries ###

#################################

## FAAB Reducation
# Reducing Player Salaries with remaining FAAB

# next step is to run this code with the df 
# then create loop to run through for each team....
# then apply same info to the keeper salary function
# do this with out being applied to csv file until after it is committed??
# add keeper selection ability - marked column


################################

#### FAAB Reduction Function ###

################################


# Function has not been updated
# working on finalizing Add keeper costs function
# same mechanics can be used on this function

def Faab_Reduction(id):

    tempdf = []                                     # create a temp dataframe

    avail_faab = team_info.loc[ id, 'faab' ]
    print ( "You current have: $" + str(avail_faab) + " of FAAB Remaining" )
    print ( "Current Roster: ")

    tempdf = rosters.loc[ rosters['team_id'] == id]
    print ( tempdf )

    # get height of Dataframe ( must be less than or equal to roster_spots )
    spots = len(tempdf.index)

    temp_list = []
    for (name, series) in tempdf.iterrows():        # iteration through each row of temp dataframe
        sal = int( str( series.iat[4] ) )                    # salary column as an int
        temp_list.append(sal)                       # creates temp list of player salaries
    print(temp_list)
    print(spots)
    print(sum(temp_list))       # sum of all player salaries
    # sum needs to be checked to ensure team can afford players for draft

    i = 0                      

    while avail_faab >= 1:

        while temp_list[i] > 1 and i < (spots - 1):
            # salary Reduction
            temp_list[i] = (temp_list[i] - faab_reduction)
            avail_faab = (avail_faab - 1)
            i = i + 1
            continue

        while i > (spots - 1):
            i = 0
            continue

        while temp_list[i] == 1 or i < 0:
            print("Salary is $1 : $" + str(avail_faab) )
            avail_faab = avail_faab
            temp_list[i] = temp_list[i]
            i = i + 1
            continue

        #else:
            #Faab_Reduction(id)



    else:
        # Maintain Salaries
        print ("out of FAAb: $" + str(avail_faab) )
        return 

# test function
Faab_Reduction(5)

##############################

#### Keeper Costs Function ###

##############################


def Add_Keeper_Salaries(id):

    global keeper_cost
    global faab_reduction
    global keeper_cost_reduction

    tempdf = []                                     # create a temp dataframe

    avail_faab = team_info.loc[ id, 'faab' ]
    print ( "You current have: $" + str(avail_faab) + " of FAAB Remaining" )
    print ( "Current Roster: ")

    tempdf = rosters.loc[ rosters['team_id'] == id]
    print ( tempdf )

    tempdf['salary'] = ( tempdf['salary'] + keeper_cost )       # Keeper Cost is applied to salaries
    print ( tempdf )

    # get height of Dataframe ( must be less than or equal to roster_spots )
    spots = len(tempdf.index)

    # Can turn off faab reductions after keeper_costs are applied
    # change Keeper_cost to 'off' in master attribute control 
    if keeper_cost_reduction == "on":

        temp_list = []
        for (name, series) in tempdf.iterrows():        # iteration through each row of temp dataframe
            sal = int( str( series.iat[4] ) )                    # salary column as an int
            temp_list.append(sal)                       # creates temp list of player salaries
        print(temp_list)
        print(spots)
        print(sum(temp_list))       # sum of all player salaries
        # sum needs to be checked to ensure team can afford players for draft
        print(temp_list[0])
        i = 0                                    # sets a value to cycle through temp_list

        while avail_faab > 0:
                                          
            while ( sum(temp_list) > spots ):        #cuts off loop when player salaries all equal $1

            # salary Reduction
                if temp_list[i] < 1:
                    print ("Error: Salary less than $1: $" + str(avail_faab) )

                elif temp_list[i] > 1:
                    temp_list[i] = temp_list[i] - faab_reduction
                    avail_faab = avail_faab - 1
                    print(temp_list)
                    print(avail_faab)

                    if ( i < (spots-1) and i >= 0 ):              # if i equals or is greater than spots or less than 0
                        i = i + 1
                        print (i)                          # reset i

                    else:                                # else iterate to next entry
                        i = 0
                        print (i)  
                    

                elif temp_list[i] == 1:
                    i = i + 1
                    avail_faab = avail_faab
                else:
                    i = i + 1
                    avail_faab = avail_faab



            
            
                    
        if avail_faab == 0:
            # When Faab is gone
            print ( "Out of Faab: $" + str(avail_faab) )
            print ( tempdf )
            return 

        else:
            # Maintain Salaries
            print ( "Error: FAAB if Negative: $" + str(avail_faab) )
            print ( tempdf )
            return  

    if keeper_cost_reduction == "off":
        # this skips Faab Reduction after Keeper Costs
        return

    else:
        print ("Error: keeper_cost_reduction not turned 'on' or 'off' ")
        return



# test function
# Add_Keeper_Salaries(5)




'''
print(rosters)

d_list = []
for (name, series) in rosters.iterrows():
    d = str(series.iat[4])
    d_list.append(d)
    print('/nCol name: ' + str(name))
    print('1st value: ' + str(series.iat[4]))



print(d_list)
'''


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

def update_rosters():

# This might need to be moved to after all calculations are copmleted or put into another file
    team_5_faab = team_info.loc[5,'faab']


# merge dataframes
    full_roster = pd.merge(rosters, team_info, on='team_id')

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
    team_1.to_csv('team1_Draft.csv', encoding='utf-8')

# create roster file by combining all team files
# once all individual files are made recombing and save over old roster file...??

# test function
# update_rosters()


############################

#### Draft Prep Function ###

############################

# This function will cycle through all required functions
# In preperation for the Draft.

def draft_prep():


    # Step 1: Confirm League Settings
    settings_confirm()

    # Step 2: Faab Reduction

    for id in team_info['team_id']:
        Faab_Reduction(id)


    # Step 3: Keeper Costs

    for id in team_info['team_id']:
        Add_Keeper_Salaries(id)

    
    # Step 4: Draft Budgets

    draft_budget()

    # Step 5: Update Team Files with Accurate Information

    update_rosters()




#################################

#### Finalize Teams for Draft ###

#################################

# the following function will complete all draft prep work
# this will be irreversible and must be take with extreme caution.

# draft_prep()