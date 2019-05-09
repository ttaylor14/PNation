# Goal is to edit the actual tempdf instead of the templist

# determine how to transform functin to eliminate the need for the temp_list

# Then clean up function to allow it to be reused in the add Keeper Sal function to reduce code length

import pandas as pd

# import files
rosters = pd.read_csv('data/rosters.csv')
team_info = pd.read_csv('data/team_info.csv')

team_info = team_info.set_index("team_id", drop=False)

# convert columns to correct types
rosters[['team_id', 'roster_id', 'salary']] = rosters[['team_id', 'roster_id', 'salary']].apply(pd.to_numeric)
team_info[['team_id', 'faab']] = team_info[['team_id', 'faab']].apply(pd.to_numeric)


def Faab_Reduction(id):

    tempdf = []                                     # create a temp dataframe

    avail_faab = team_info.loc[id, 'faab']
    print("You current have: $" + str(avail_faab) + " of FAAB Remaining")
    print("Current Roster: ")

    tempdf = rosters.loc[rosters['team_id'] == id]
    print(tempdf)

    temp_list = []
    for (name, series) in tempdf.iterrows():        # iteration through each row of temp dataframe
        sal = int(str(series.iat[4]))                    # salary column as an int
        temp_list.append(sal)                       # creates temp list of player salaries
    print(temp_list)
    print(sum(temp_list))       # sum of all player salaries
    # sum needs to be checked to ensure team can afford players for draft

    i = 0

    while avail_faab > 0:                    # If you have faab
        while sum(temp_list) > len(temp_list):         # if the sum of all salaries is greater than the number of players
                                            # Goal is to see if all $1
            while temp_list[i] == 1:            # when a salary = 1 skip
                i = i + 1
                continue

            else:
                if avail_faab > 0:
                    temp_list[i] = temp_list[i] - 1         # reduce Salary
                    avail_faab = avail_faab - 1          # reduce faab
                    i = i + 1               # next entry
                    print("my faab" + str(avail_faab))
                    print(temp_list)
                    if i >= (len(temp_list) - 1):  # when we reach the last entry
                        i = 0             # reset to 0
                break

        else:
            print("Salaries are all $1")
            break
    # tempdf.salary = [temp_list[item] for item in tempdf.salary]
    print(temp_list)



# test function
Faab_Reduction(5)
