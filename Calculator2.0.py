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

######################################

### create Team Rosters by team_id ###

######################################

# This might need to be moved to after all calculations are copmleted or put into another file
team_5_faab = team_info.loc[5,'faab']


# merge dataframes
full_roster = pd.merge(rosters, team_info, on='team_id')


# at the end export each team to own file in teams Folder
# create roster file by combining all team files


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

def Faab_Reduction():
    global faab
    global salaries

    while faab >= 0:
        if faab == 0:
            # When Faab is gone
            print (faab)
            print (salaries)
            return 

        if faab > 0:
            if salaries > 1:
                # salary Reduction
                salaries = (salaries - faab_reduction)
                faab = (faab - 1)
            else:
                faab = faab
                salaries = salaries

        else:
            print("Error, FAAB is Negative")

    else:
        # Maintain Salaries
        print (faab)
        print (salaries)
        return faab, salaries




def Add_Keeper_Salaries(id):

    global keeper_cost
    global faab_reduction
    global keeper_cost_reduction

    avail_faab = team_info.loc[ id, 'faab' ]
    print ( avail_faab )

    tempdf = rosters.loc[ rosters['team_id'] == id]
    print ( tempdf )

    tempdf['salary'] = tempdf['salary'] + keeper_cost
    print ( tempdf )

    # get height of Dataframe ( must be less than or equal to roster_spots )
    spots = len(tempdf.index)

    # Can turn off faab reductions after keeper_costs are applied
    # change Keeper_cost to 'off' in master attribute control 
    if keeper_cost_reduction == "on":

        while avail_faab > 0:

            # salary Reduction
            for index, row in tempdf.iterrows():
                if row['salary'] > 1:
                    tempdf[index ,'salary'] = tempdf[index ,'salary'] - faab_reduction
                    avail_faab = avail_faab - 1
                elif row == 1:
                    # salary has reach $1
                    tempdf[row ,'salary']
                elif row < 1:
                    print ("Error: Salary less than $1")
                else:
                    print ("Error")



        if avail_faab == 0:
            # When Faab is gone
            print ( "Out of Faab" )
            print ( avail_faab, tempdf )
            return 

        else:
            # Maintain Salaries
            print ( "Error: FAAB if Negative" )
            print ( avail_faab, tempdf )
            return 

    if keeper_cost_reduction == "off":
        # this skips Faab Reduction after Keeper Costs
        return

    else:
        print ("Error: keeper_cost_reduction not turned 'on' or 'off' ")
        return



# this code will cycle through all teams
# for id in team_info['team_id']:
    #Add_Keeper_Salaries(id)

Add_Keeper_Salaries(5)


#################################

#### Calculate Draft Salaries ###

#################################
