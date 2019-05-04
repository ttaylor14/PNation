## PNation.py

import pandas as pd


####################

#### Import Data ###

####################

faab = 15
salaries = 45

# Master attribute controls
keeper_cost = 5
draft_budget = 300
roster_spots = 25
il_spots = 5
# faab reduction - how much player salaries are decreased per dollar of faab
faab_reduction = 1

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




def Add_Keeper_Salaries(faab, salaries):

    #global faab
    #global salaries
    #global keeper_cost

    salaries = (salaries + keeper_cost)

    # Add a way to turn off faab reductions after keeper_costs are applied

    while faab > 0:

        # salary Reduction
        salaries = salaries - faab_reduction
        faab = faab - 1


    if faab == 0:
        # When Faab is gone
        print "Out of Faab"
        print faab, salaries
        return faab, salaries

    else:
        # Maintain Salaries
        print "Error: FAAB if Negative"
        print faab, salaries
        return faab, salaries



#Faab_Reduction()
#print(faab, salaries)


print team_5[['faab', 'salary']]

#print Add_Keeper_Salaries(team_5['faab'], team_5['salary'])
team_5.apply(lambda x: Add_Keeper_Salaries(team_5_faab, x['salary']), axis=1)


print team_5[['faab', 'salary']]


#team_5_test = team_5
#team_5_test['faab', 'salary'] = team_5['faab', 'salary'].apply(Add_Keeper_Salaries(team_5['faab', 'salary'])



#################################

#### Calculate Draft Salaries ###

#################################
